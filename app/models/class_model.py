import uuid
from sqlalchemy import Column, String, Date, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from database import Base
from .associations import user_classDB, class_roomDB

class ClassDB(Base):
    __tablename__ = "class"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    type = Column(String(255))
    name = Column(String(255))
    time_frame = Column(TIMESTAMP)
    day = Column(Date)

    users = relationship("UserDB", secondary=user_classDB, back_populates="classes")
    rooms = relationship("RoomDB", secondary=class_roomDB, back_populates="classes")