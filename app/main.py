from fastapi import FastAPI,HTTPException, Depends , status,Query
from pydantic import BaseModel
from typing import Annotated 
from . import models

from app.database import engine,sessionmaker
from sqlalchemy.orm import Session 
app = FastAPI()
from  app.services.postService import (_dellPosts,_createPost,_getPosts,_getPostBySlug,count_posts)
from slugify import slugify





models.Base.metadata.create_all(bind=engine)

class postBase(BaseModel):
    post_title:str
    post_content:str
    post_excerpt:str
class postBaseUpdate(BaseModel):
    post_title:str
    post_content:str
    post_excerpt:str
    slug:str

def get_db():
    db = sessionmaker()
    try:
        yield db
    finally:
        db.close()
db_dependency = Annotated[Session, Depends(get_db)]

@app.get("/delPost/" , status_code= status.HTTP_200_OK)
async def dellPosts(db:db_dependency):
   _dellPosts(db)

@app.post("/AddPosts/", status_code= status.HTTP_200_OK)
async def createPost(post:postBase   ,db:db_dependency):
   _createPost(post,db)
   
@app.get("/ListAllPosts/", status_code= status.HTTP_200_OK)
async def getPosts(db:db_dependency,limit=2):
    return _getPosts(db,limit)



@app.get("/postbySlug/", status_code= status.HTTP_200_OK)
async def getBySlug(db:db_dependency, slug:str):
   _getPostBySlug(db,slug)

@app.get("/count/",status_code= status.HTTP_200_OK)
async def _count(db:db_dependency):
    return count_posts(db)

@app.post("/updatePost/",status_code= status.HTTP_200_OK)
async def updatePost(post:postBaseUpdate   ,db:db_dependency):
   # post_data: dict = models.Post(**post.model_dump())
    _post: dict =  post.model_dump()
    db_post = _getPostBySlug(db,_post.get("slug"))
    if(_post["post_title"] != "-1"):
        setattr(db_post, "post_title", _post["post_title"])
        setattr(db_post, "post_slug", slugify( _post["post_title"]))
    if(_post["post_excerpt"] != "-1"):
        setattr(db_post, "post_excerpt", _post["post_excerpt"])
    if(_post["post_content"] != "-1"): 
        setattr(db_post, "post_content", _post["post_content"])
    db.commit()
    db.refresh(db_post)
  
