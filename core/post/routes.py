from fastapi import APIRouter, Depends , HTTPException ,Query
from sqlalchemy.orm import Session
from sqlalchemy import desc, asc
from dependencies import get_db,get_current_user,get_pagination,paginate_query
from core.user.models import User
from .schema import CreateUpdatePost
from .models import Post
from .dependency import get_post_for_user
from typing import Optional

post_router = APIRouter()
@post_router.post('/post')
def create_post(post_data:CreateUpdatePost,db: Session = Depends(get_db),user:User = Depends(get_current_user)):
    post = Post(title=post_data.title,content= post_data.content,author_id = user.id)
    db.add(post)
    db.commit()
    return{
        "data" : post_data
    }









@post_router.get('/posts')
def list_post(db:Session = Depends(get_db),user : User=Depends(get_current_user),page: dict = Depends(get_pagination),order: str = Query("asc", alias="order")):

    allowed_sort_orders = ["asc", "desc"]

    if order.lower() not in allowed_sort_orders:
        raise HTTPException(status_code=400, detail="Invalid sort order")

    posts = db.query(Post)

    paginated_result = paginate_query(
        posts.order_by(
            Post.title.asc() if order.lower() == "asc" else Post.title.desc()
        ),
        page["page"],
        page["page_size"],
    )


    paginated_posts = paginated_result.items
    total_pages = paginated_result.pages

    current_page = page["page"]
    next_page = current_page + 1 if current_page < total_pages else None
    prev_page = current_page - 1 if current_page > 1 else None

    base_url = f"/posts?page_size={page['page_size']}"
    next_page_url = f"{base_url}&page={next_page}" if next_page else None
    prev_page_url = f"{base_url}&page={prev_page}" if prev_page else None


    response_data = {
        "data": [post.__dict__ for post in paginated_posts],
        "page_info": {
            "current_page": current_page,
            "total_pages": total_pages,
            "next_page": next_page_url,
            "prev_page": prev_page_url,
        }
    }

    return response_data













@post_router.get("/post/{post_id}")
def view_post(post_id:str , db:Session= Depends(get_db),user: User=Depends(get_current_user)):
    post = db.query(Post).filter(Post.id==post_id).first()
    if not post:
        raise HTTPException(status_code=404,detail="Post not found")
    return{
        "data" : post.__dict__
    }

@post_router.put('/post/{post_id}')
def edit_post(post_id:str, post_data: CreateUpdatePost, post:Post = Depends(get_post_for_user),db:Session = Depends(get_db)):
    post.title = post_data.title
    post.content = post_data.content
    db.commit()
    return{
        "data" : post_data
    }

@post_router.delete('/post/{post_id}')
def delete_post(post_id:str, post:Post = Depends(get_post_for_user),db:Session = Depends(get_db)):
    db.delete(post)
    db.commit()
    return{
        "message" : "Post deleted successfully"
    }
