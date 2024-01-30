from core.post.models import Post
from core.user.models import User

def test_create_post():
    post = Post(title = "Hello world", content= "This is a post")
    assert post.title == "Hello world"
    assert post.content == "This is a post"
   
def test_user_posts_relationship():
    user = User(username = "user", email="user@email.com",hashed_password="password")
    post = Post(title = "Hello world", content= "This is a post",author=user)
    assert post.author == user