from pydantic import BaseModel
from datetime import datetime

class MessageCreate(BaseModel):
    content: str
    role: str
    type: str

class Message(MessageCreate):
    id: int
    date: datetime

    class Config:
         from_attributes = True