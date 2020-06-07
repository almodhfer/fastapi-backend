from typing import Optional

from pydantic import BaseModel


class OrderBase(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None


# Properties to receive on order creation
class OrderCreate(OrderBase):
    title: str


# Properties to receive on order update
class OrderUpdate(OrderBase):
    pass


# Properties shared by models stored in DB
class OrderInDBBase(OrderBase):
    id: int
    title: str
    owner_id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Order(OrderInDBBase):
    pass


# Properties properties stored in DB
class OrderInDB(OrderInDBBase):
    pass
