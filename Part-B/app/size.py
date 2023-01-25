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
    error_flag = True
    topic_matched = 0
    for topic in consumer.topics:
        if(topic.topic_name == topic_name):
            topic_matched = topic
            error_flag = False
            break
    
    if(error_flag):
        raise HTTPException(status_code=404, detail="Topic not found")

    # taking out messages for topic
    consumer_messages = db.query(Message).filter(
        Message.topic_id == topic_matched
    ).all()

    # message = consumer_messages[consumer.last_message_index]
    size = len(consumer_messages) - consumer.last_message_index
    # consumer.update({'last_message_index': consumer.last_message_index + 1})
    # db.commit()    

    return size





