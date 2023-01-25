from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import List
from core import database
from models import Producer, Consumer, Topic, Message

get_db = database.get_db

router = APIRouter(
    prefix="/example",
    tags=['example']
)


# Get all items
@router.get('/')
def all(db: Session = Depends(get_db),):
    topics = db.query(Topic).filter(
        # Topic.topic_name == ''
    ).all()
    return topics


@router.post('/add-topic/{topic}', status_code=status.HTTP_201_CREATED,)
def create(topic: str, db: Session = Depends(get_db)):
    new_topic = Topic(topic_name=topic)
    db.add(new_topic)
    db.commit()
    db.refresh(new_topic)
    return new_topic
