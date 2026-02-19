import uuid
from sqlalchemy import Column, String, Float
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from database import Base
from .associations import class_roomDB

class RoomDB(Base):
    __tablename__ = "room"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(255))
    posX = Column(Float)
    posY = Column(Float)

    classes = relationship("ClassDB", secondary=class_roomDB, back_populates="rooms")
