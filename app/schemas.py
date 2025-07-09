from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime

class MessageBase(BaseModel):
    content: str
    role: str
    type: str

class MessageCreate(MessageBase):
    session_id: Optional[str] = None

class Message(MessageBase):
    id: int
    session_id: Optional[str] = None
    date: datetime

    class Config:
         from_attributes = True

class Session(BaseModel):
    id: str
    created_at: Optional[datetime]
    messages: Optional[List[Message] ]= []

    class Config:
        from_attributes = True