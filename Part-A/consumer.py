from fastapi import FastAPI
from pydantic import BaseModel
# from fastapi import APIRouter

# router = APIRouter()

app = FastAPI()

class Consumer(BaseModel):
    id: int
    topic: str


# POST for registering user
@app.post('/{consumer_id}/{topic}/register')
def register_consumer(consumer_id: int, topic):
    return {'Data':{'ConsummerId':consumer_id,
                    'Topic':topic}}


# GET for dequeue
@app.get('/{consumer_id}/{topic}')
def dequeue_topic(consumer_id: int, topic):
    return {'Data':{'ConsummerId':consumer_id,
                    'Topic':topic}}

