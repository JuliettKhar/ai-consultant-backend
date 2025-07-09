from sqlalchemy import Column, Integer, String, DateTime
from app.database import Base
from datetime import datetime

class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, index=True)
    role = Column(String, default="user")
    date = Column(DateTime, default=datetime.utcnow)
    type = Column(String, index=True)