from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import List
from core import database
from models import Producer, Producer, Topic, Message

get_db = database.get_db

router = APIRouter(
    prefix="/producer",
    tags=['producer']
)


# posting message
@router.post('/produce/{topic_name}/{producer_id}/{message}')
def all(topic_name, producer_id, message, db: Session = Depends(get_db),):
    producer = db.query(Producer).filter(
        Producer.producer_id == producer_id
    ).first()
    if producer is None:
        raise HTTPException(status_code=404,detail="producer not found")
    topic_matched = producer.topics
    # print(topic_matched)
    if (topic_matched.topic_name == topic_name):
        # add message for topic
        new_message = Message(topic_id=topic_matched.topic_id, message=message)
        db.add(new_message)
        db.commit()
        db.refresh(new_message)
        return new_message
    else:
        raise HTTPException(status_code=404, detail="Topic not found")


# Register producer with topics
@router.post('/register/{topic_name}', status_code=status.HTTP_201_CREATED,)
def create(topic_name: str, db: Session = Depends(get_db)):
    # check topic in db
    topic = db.query(Topic).filter(Topic.topic_name == topic_name).first()
    if topic is None:
        # create new topic
        new_topic = Topic(topic_name=topic_name)
        db.add(new_topic)
        db.commit()
        db.refresh(new_topic)
        topic = new_topic
    new_producer = Producer(topic_id=topic.topic_id)
    db.add(new_producer)
    db.commit()
    db.refresh(new_producer)
    print(new_producer.producer_id)
    return new_producer
