from pydantic import BaseModel

class MessageCreate(BaseModel):
    content: str

class Message(MessageCreate):
    id: int
    class Config:
         from_attributes = True