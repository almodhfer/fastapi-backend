from fastapi import APIRouter
from app.order.api import router as order_router
from app.profile import userRouter
from app.profile import loginRouter
api_router = APIRouter()
api_router.include_router(loginRouter, tags=["login"], prefix='/login')
api_router.include_router(userRouter, tags=["users"], prefix='/users')
api_router.include_router(order_router, tags=["orders"], prefix='/orders')
