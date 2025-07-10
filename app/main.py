from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app import schemas
from app import crud
from app import models
from app.database import SessionLocal, engine, Base
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://juliettkhar.github.io"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

@app.post("/messages", response_model=schemas.Message)
def create_message(message: schemas.MessageCreate, db: Session = Depends(get_db)):
    return crud.create_message(db, message=message)

@app.get("/messages", response_model=List[schemas.Message])
def get_messages(session_id: Optional[str] = None, db: Session = Depends(get_db)):
    return crud.get_messages(db, session_id=session_id)
    # query = db.query(models.Message)
    # if session_id:
    #     query = query.filter(models.Message.session_id == session_id)
    # return query.order_by(models.Message.date).all()


@app.post("/sessions", response_model=schemas.Session)
def create_session(db: Session = Depends(get_db)):
    new_session = models.Session()
    db.add(new_session)
    db.commit()
    db.refresh(new_session)
    return new_session
