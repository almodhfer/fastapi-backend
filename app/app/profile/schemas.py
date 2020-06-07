from typing import Optional

from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    full_name: str
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    email: Optional[str]


# Properties to receive on user creation
class UserCreate(UserBase):
    password: str

# Properties to receive on user update


class UserUpdate(UserBase):
    password: Optional[str]


# Properties shared by models stored in DB
class UserInDBBase(UserBase):
    id: int
    username: str
    full_name: str
    is_active: Optional[bool]
    is_superuser: Optional[bool]
    email: Optional[str]

    class Config:
        orm_mode = True


# Properties to return to client
class User(UserInDBBase):
    pass


# Properties properties stored in DB
class UserInDB(UserInDBBase):
    pass


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenPayload(BaseModel):
    sub: Optional[int] = None
