# pydantic models different from sqlalchemy models
import datetime as _dt
import pydantic as _pydantic
from typing import List

# shape the model


class _PostBase(_pydantic.BaseModel):
    title: str
    content: str


# {"title": "this is a title", "content": "some content for post"}


class PostCreate(_PostBase):
    pass


# {
#     "id": 1,
#     "owner_id": 23,
#     "title": "this is a title",
#     "content": "some content for post",
#     "date_created": "12-12-12",
#     "date_last_updated": "12-12-12"
# }


class Post(_PostBase):
    id: int
    owner_id: int
    date_created: _dt.datetime
    date_last_updated: _dt.datetime

    # By default orm_mode is set to false, SQLAlchemy by default does lazy loading as we don't want lazy loading here
    # When we load our user, we want the POST to come with it
    class Config:
        orm_mode = True


class _UserBase(_pydantic.BaseModel):
    email: str


class UserCreate(_UserBase):
    password: str


# {"email": "jesse@hubzero.com", "id": 1, "is_active": true, "posts": []}


# Read User in. Empty array for posts by default
class User(_UserBase):
    id: int
    is_active: bool
    posts: List[Post] = []

    # Don't want lazy loading
    class Config:
        orm_mode = True
