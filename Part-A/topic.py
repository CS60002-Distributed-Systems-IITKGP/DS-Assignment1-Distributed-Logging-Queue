from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/topics")
def get_topics():
    return {"topics": ['topic1', 'topic2']}


class Topic(BaseModel):
    name: str
    
@app.post("/topics/{topic_string}")
def create_topic(topic_string):
    return {"Topic":topic_string}