from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.db.curd_base import CRUDBase
from app.order.models import Order
from app.order.schema import OrderCreate, OrderUpdate


class CRUDOrder(CRUDBase[Order, OrderCreate, OrderUpdate]):
    pass


order = CRUDOrder(Order)
