from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import List
from core import database
from models import Producer, Consumer, Topic, Message

get_db = database.get_db

router = APIRouter(
    prefix="/size",
    tags=['size']
)


# Get all items
@router.get('/{topic_name}/{consumer_id}')
def all(topic_name, consumer_id, db: Session = Depends(get_db),):
    consumer = db.query(Consumer).filter(
        Consumer.consumer_id == consumer_id
    ).first()
    if consumer is None:
        raise HTTPException(status_code=404, detail="consumer not found")
    # error_flag = True
    topic_matched = consumer.topics
    # print(consumer.topics)
    if (topic_matched.topic_name == topic_name):
        # taking out messages for topic
        consumer_messages = db.query(Message).filter(
            Message.topic_id == topic_matched.topic_id
        ).all()
        # message = consumer_messages[consumer.last_message_index]
        size = len(consumer_messages) - consumer.last_message_index
        return size
    else:
        raise HTTPException(status_code=404, detail="Topic not found")
