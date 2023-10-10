
from sqlalchemy import Boolean,Column,Integer,String,DateTime, func
from app.database import Base
from pydantic import BaseModel
class postBase(BaseModel):
    post_title:str
    post_content:str
    post_excerpt:str
    post_slug:str

class Post(Base):
    __tablename__='posts'
    ID = Column(Integer , primary_key=True,index=True) 
    post_author = Column(Integer , default= 1) 
    post_date = Column(DateTime, default=func.now() )
    post_content = Column(String(200) ,  nullable= True)
    post_title = Column(String(200) , nullable= True)
    post_excerpt = Column(String(200) , nullable= True)
 #   post_slug = Column(String(200) , nullable = False ,index=True)
    post_status = Column(Integer, default= 0)
    post_slug = Column(String(200) , nullable = False ,index=True,unique= True)
    post_icon_image = Column(String(200),nullable= True)
   