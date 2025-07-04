from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app import schemas
from app import crud
from app.database import SessionLocal, engine, Base

import os
print("DB ENV:", os.getenv("DB_HOST"), os.getenv("DB_USER"), os.getenv("DB_PASSWORD"))


Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/messages", response_model=schemas.Message)
def create_message(message: schemas.MessageCreate, db: Session = Depends(get_db)):
    return crud.create_message(db, message=message)

@app.get("/messages", response_model=list[schemas.Message])
def read_messages(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_messages(db, skip=skip, limit=limit)