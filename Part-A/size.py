from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import HTTPException


app = FastAPI()
topics = []

# GET for getting size for each consumer
@app.get('/{consumer_id}/{topic_id}/size')
def dequeue_topic(consumer_id: int, topic_id: int):
    if topic_id not in topics:
        raise HTTPException(status_code=404, detail="Topic not found")
    return {'Data':{'ConsummerId':consumer_id,
                    'Topic':topic_id}}