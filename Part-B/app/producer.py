from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import List
from core import database
from models import Producer, Consumer, Topic, Message

get_db = database.get_db

router = APIRouter(
    prefix="/producer",
    tags=['producer']
)

