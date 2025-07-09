from sqlalchemy.orm import Session
from app import models
from app import schemas


def get_messages(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Message).offset(skip).limit(limit).all()

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