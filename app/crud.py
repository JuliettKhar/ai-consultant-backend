from sqlalchemy.orm import Session
from app import models
from app import schemas
import os
from dotenv import load_dotenv
load_dotenv()


def get_messages(db: Session, session_id: str):
    query = db.query(models.Message)
    if session_id:
        query = query.filter(models.Message.session_id == session_id)
    return query.order_by(models.Message.date).all()
    # return db.query(models.Message).offset(skip).limit(limit).all()

def create_message(db: Session, message: schemas.MessageCreate):
    db_message = models.Message(
        content=message.content,
        role=message.role,
        type=message.type,
        session_id=message.session_id
    )
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message

def get_api_key():
    return os.getenv("API_KEY")