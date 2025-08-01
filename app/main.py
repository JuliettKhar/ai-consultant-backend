from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app import schemas
from app import crud
from app import models
from app.database import SessionLocal, engine, Base
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
from app.database import get_db

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/messages", response_model=schemas.Message)
def create_message(message: schemas.MessageCreate, db: Session = Depends(get_db)):
    return crud.create_message(db, message=message)

@app.get("/messages", response_model=List[schemas.Message])
def get_messages(session_id: Optional[str] = None, db: Session = Depends(get_db)):
    return crud.get_messages(db, session_id=session_id)


@app.post("/sessions", response_model=schemas.Session)
def create_session(db: Session = Depends(get_db)):
    new_session = models.Session()
    db.add(new_session)
    db.commit()
    db.refresh(new_session)
    return new_session

@app.get("/sessions", response_model=List[schemas.Session])
def get_sessions(db: Session = Depends(get_db)):
    return crud.get_sessions(db)

@app.delete("/sessions/{session_id}")
def delete_session(session_id: str, db: Session = Depends(get_db)):
    return crud.delete_session(session_id=session_id, db=db)
