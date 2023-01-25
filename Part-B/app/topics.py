from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import List
from core import database
from models import Producer, Consumer, Topic, Message
from pydantic import BaseModel

get_db = database.get_db

router = APIRouter(
    prefix="/topics",
    tags=['topics']
)

# class Topic(BaseModel):
#     name: str

# Get all items
@router.get('/')
def all(db: Session = Depends(get_db),):
    topics = db.query(Topic).filter(
        # Topic.topic_name == ''
    ).all()
    if len(topics) == 0:
        raise HTTPException(status_code=404, detail="No topics found")
    return topics
 

@router.post('/{topic}', status_code=status.HTTP_201_CREATED,)
def create(topic: str, db: Session = Depends(get_db)):
    new_topic = Topic(topic_name=topic)
    db.add(new_topic)
    db.commit()
    db.refresh(new_topic)
    return new_topic