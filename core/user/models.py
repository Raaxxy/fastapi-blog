from sqlalchemy import Integer,Column,ForeignKey,String , ARRAY
from sqlalchemy.orm import relationship
from config import get_settings
from sqlalchemy.dialects.postgresql import UUID
from database import Base 
from datetime import datetime ,timedelta
import uuid
import bcrypt
import jwt



class User(Base):
    __tablename__ = "user"

    id = Column(UUID(as_uuid=True), primary_key=True,default=uuid.uuid4)
    username = Column(String,unique=True,index=True)
    email = Column(String,unique=True,index=True)
    hashed_password = Column(String)
    tags = Column(ARRAY(String), default=[])
    
    def hash_password(self,password:str):
        self.hashed_password = bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt()).decode('utf-8')
    
    def verify_password(self,password:str):
        return bcrypt.checkpw(password.encode('utf-8'),self.hashed_password.encode('utf-8'))
    
    def generate_token(self):
        expiration = datetime.utcnow() + timedelta(hours=24)
        payload = {
            "sub" : str(self.id),
            "exp" : expiration
        }
        return jwt.encode(payload,f"{get_settings().SECRET_KEY}", algorithm = "HS256")
        
    def add_tag(self, tag: str):
        if tag not in self.tags:
            self.tags.append(tag)


    def remove_tag(self, tag: str):
        if tag in self.tags:
            self.tags.remove(tag)

