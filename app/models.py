from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from app.database import Base
from datetime import datetime
import uuid

from sqlalchemy.orm import relationship


class Session(Base):
    __tablename__ = "session"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    created_at = Column(DateTime, default=datetime.utcnow)

    messages = relationship("Message", back_populates="session")

class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(String, ForeignKey("session.id"), nullable=True)
    content = Column(String, index=True)
    role = Column(String, default="user")
    date = Column(DateTime, default=datetime.utcnow)
    type = Column(String, index=True)

    session = relationship("Session", back_populates="messages")