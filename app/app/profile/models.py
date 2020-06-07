from sqlalchemy import BigInteger, Column, String, Boolean
from app.db.base import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(BigInteger, primary_key=True)
    username = Column(String)
    password = Column(String)
    full_name = Column(String)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
    email = Column(String, nullable=True)
