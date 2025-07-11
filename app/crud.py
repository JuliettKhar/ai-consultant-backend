from sqlalchemy.orm import Session
from app import models
from app import schemas
from app.database import get_db
from fastapi import Depends
from fastapi import HTTPException


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

def get_sessions(db: Session = Depends(get_db)):
    return db.query(models.Session).order_by(models.Session.created_at.desc()).all()

def delete_session(session_id: str, db: Session = Depends(get_db)):
    session = db.query(models.Session).filter(models.Session.id == session_id).first()
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    db.delete(session)
    db.commit()
    return {"detail": "Session deleted"}