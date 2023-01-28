from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import HTTPException
# from fastapi import APIRouter

# router = APIRouter()

app = FastAPI()

class Consumer(BaseModel):
    id: int
    topic: str

topics = []

# POST for registering user
@app.post('/{consumer_id}/{topic_id}/register')
def register_consumer(consumer_id: int, topic_id: int):
    if topic_id not in topics:
        raise HTTPException(status_code=404, detail="Topic not found")
    return {'Data':{'ConsummerId':consumer_id,
                    'Topic':topic_id}}


# GET for dequeue
@app.get('/{consumer_id}/{topic_id}')
def dequeue_topic(consumer_id: int, topic_id: int):
    if topic_id not in topics:
        raise HTTPException(status_code=404, detail="Topic not found")
    return {'Data':{'ConsummerId':consumer_id,
                    'Topic':topic_id}}

