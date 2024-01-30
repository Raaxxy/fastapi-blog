from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from dependencies import get_db,get_current_user
from core.user.models import User
from .schema import CreateUpdatePost
from .models import Post


post_router = APIRouter()
@post_router.post('/post')
def create_post(post_data:CreateUpdatePost,db: Session = Depends(get_db),user:User = Depends(get_current_user)):
    post = Post(title=post_data.title,content= post_data.content,author_id = user.id)
    db.add(post)
    db.commit()
    return{
        "data" : post_data
    }



