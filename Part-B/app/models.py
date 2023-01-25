from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from core.database import Base
from sqlalchemy.orm import relationship
import datetime


class Topic(Base):
    __tablename__ = 'topics'

    topic_id = Column(Integer, primary_key=True, index=True)
    topic_name = Column(String)


class Producer(Base):
    __tablename__ = 'producers'

    producer_id = Column(Integer, primary_key=True, index=True)
    topic_id = Column(Integer, ForeignKey('topics.topic_id'))

    topics = relationship("Topic", backref="producers")


class Consumer(Base):
    __tablename__ = 'consumers'

    consumer_id = Column(Integer, primary_key=True, index=True)
    topic_id = Column(Integer, ForeignKey('topics.topic_id'))

    last_message_index = Column(Integer, default=0)

    topics = relationship("Topic", backref="consumers")


class Message(Base):
    __tablename__ = 'messages'

    message_id = Column(Integer, primary_key=True, index=True)
    topic_id = Column(Integer, ForeignKey('topics.topic_id'))
    message = Column(String)
    created_date = DateTime(default=datetime.datetime.utcnow)

    topics = relationship("Topic", backref="messages")
