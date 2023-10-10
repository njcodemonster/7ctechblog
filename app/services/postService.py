from fastapi import FastAPI,HTTPException, Depends , status,Query
from pydantic import BaseModel
from typing import Annotated
import app.models
from slugify import slugify

from sqlalchemy.orm import Session 


def _dellPosts(db):
    db_posts = app.models.Post()
    stm = db_posts.__table__.delete()
    db.execute(stm) 
    db.commit()
    return "deleted all"

def _createPost(post   ,db):
    db_post = app.models.Post(**post.model_dump())
    setattr(db_post, "post_slug", slugify(db_post.post_title))
    db_post = db.add(db_post)
    db.commit()
    return db_post
def count_posts(db: Session) -> int:
    total = db.query(app.models.Post).count()
    return total
def _getPosts(db,limit = 4):
    db_posts = app.models.Post()
    db_posts = db.query(app.models.Post).limit(limit).all()
    return db_posts
def _getPostBySlug(db,slug):
    db_posts = app.models.Post()
    db_posts = db.query(app.models.Post).filter(app.models.Post.post_slug ==slug).first()
    return db_posts