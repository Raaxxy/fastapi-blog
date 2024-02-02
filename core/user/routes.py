import re
from fastapi import APIRouter, HTTPException,Depends, Query
from sqlalchemy import func, cast, ARRAY, String
from sqlalchemy.orm import Session,joinedload
from .models import User
from core.post.models import Post
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

#potential dashboard feature

# @user_router.get('/dashboard')
# def dashboard(db: Session = Depends(get_db), user: User = Depends(get_current_user),
#               page: dict = Depends(get_pagination), order: str = Query("asc", alias="order")):

#     allowed_sort_orders = ["asc", "desc"]

#     if order.lower() not in allowed_sort_orders:
#         raise HTTPException(status_code=400, detail="Invalid sort order")

#     user_tags = user.tags

#     if not user_tags:
#         return {"message": "User has no followed tags"}
   
#     all_posts = db.query(Post)
#     print(all_posts)

#     posts = all_posts.filter(Post.tags.op('&&')(user_tags))
#     print(posts)


#     sort_column = Post.title.asc() if order.lower() == "asc" else Post.title.desc()
#     paginated_result = paginate_query(
#         posts.order_by(sort_column),
#         page["page"],
#         page["page_size"],
#     )

#     paginated_posts = paginated_result.items
#     total_pages = paginated_result.pages

#     current_page = page["page"]
#     next_page = current_page + 1 if current_page < total_pages else None
#     prev_page = current_page - 1 if current_page > 1 else None

#     base_url = f"/dashboard?page_size={page['page_size']}&order={order}"
#     next_page_url = f"{base_url}&page={next_page}" if next_page else None
#     prev_page_url = f"{base_url}&page={prev_page}" if prev_page else None

#     response_data = {
#         "data": [post.__dict__ for post in paginated_posts],
#         "page_info": {
#             "current_page": current_page,
#             "total_pages": total_pages,
#             "next_page": next_page_url,
#             "prev_page": prev_page_url,
#         }
#     }

#     return response_data
