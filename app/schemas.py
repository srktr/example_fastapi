from pydantic import BaseModel, EmailStr, ConfigDict, Field
from datetime import datetime
from typing import Optional, Annotated




class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime    

class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int  
    owner: UserOut

    class Config:
        from_attributes = True

class PostOut(BaseModel):
    Post: Post
    votes: int

    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    model_config = ConfigDict(coerce_numbers_to_str=True)
    access_token: str
    token_type: str

class TokenData(BaseModel):
    model_config = ConfigDict(coerce_numbers_to_str=True)
    id: str   
 
class Vote(BaseModel):
    post_id: int
    dir: Annotated[int, Field(le=1)] 