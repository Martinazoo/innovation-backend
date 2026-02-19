import uuid
from sqlalchemy import Column, String, Float
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from database import Base
from .associations import user_classDB

class UserDB(Base):
    __tablename__ = "user"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(255), nullable=False)
    surname = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    bachelor_degree = Column(String(255))
    posX = Column(Float)
    posY = Column(Float)

    classes = relationship("ClassDB", secondary=user_classDB, back_populates="users")
