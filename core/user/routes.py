from fastapi import APIRouter, HTTPException,Depends, Query
from sqlalchemy.orm import Session

from core.post.routes import get_blogs_by_tags
from .models import User
from dependencies import get_db,get_current_user, get_pagination, paginate_query
from .schema import UserCreate,UserLogin, Token
from typing import List

user_router = APIRouter()

@user_router.post('/signup')
def signup(user_data:UserCreate,db: Session = Depends(get_db)):
    user = User(username=user_data.username, email=user_data.email, tags=user_data.tags)
    user.hash_password(user_data.password)
    db.add(user)
    db.commit()
    return{
        "message": "User has been created successfully"
    }

@user_router.post('/login')
def login(user_data: UserLogin,db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == user_data.username).first()
    if user is None or not user.verify_password(user_data.password):
        raise HTTPException(status_code = 401, default="Invalid Credentials")
    token = user.generate_token()
    return Token(access_token=token,token_type='bearer')

@user_router.post('/tags/add')
def add_tags(tags: List[str], user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    for tag in tags:
        user.add_tag(tag)
    db.commit()
    return {
        "message": "Tags added successfully"
    }

@user_router.post('/tags/remove')
def remove_tags(tags: List[str], user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    for tag in tags:
        user.remove_tag(tag)
    db.commit()
    return {
        "message": "Tags removed successfully"
    }


