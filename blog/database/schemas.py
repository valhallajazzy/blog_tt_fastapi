from pydantic import BaseModel
from pydantic import field_validator, EmailStr
from datetime import datetime


class Validators:
    @classmethod
    def checking_values_for_100(cls, value):
        if len(value) > 100:
            raise ValueError(f'Incorrect value {value}')
        return value


class AuthorBase(BaseModel, Validators):
    first_name: str
    last_name: str
    email: EmailStr

    @field_validator('first_name','last_name')
    @classmethod
    def names_validate(cls, value):
        Validators.checking_values_for_100(value)
        return value


class DeleteBase(BaseModel):
    id: int


class PostUpdate(DeleteBase):
    title: str
    text: str


class PostBase(PostUpdate):
    author_id: int
    category_id: int


class CategoryBase(BaseModel):
    category_name: str

    @field_validator('category_name')
    @classmethod
    def category_name_validate(cls, category_name):
        Validators.checking_values_for_100(category_name)
        return category_name


class TagBase(BaseModel):
    title: str

    @field_validator('title')
    @classmethod
    def title_validate(cls, title):
        Validators.checking_values_for_100(title)
        return title
