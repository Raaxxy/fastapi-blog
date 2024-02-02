from typing import List
from pydantic import BaseModel

class CreateUpdatePost(BaseModel):
    title:str
    content:str
    tags:List[str]