from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from database import Base

user_classDB = Table(
    "user_class",
    Base.metadata,
    Column("user_id", UUID(as_uuid=True), ForeignKey("user.id"), primary_key=True),
    Column("class_id", UUID(as_uuid=True), ForeignKey("class.id"), primary_key=True),
)

class_roomDB = Table(
    "class_room",
    Base.metadata,
    Column("class_id", UUID(as_uuid=True), ForeignKey("class.id"), primary_key=True),
    Column("room_id", UUID(as_uuid=True), ForeignKey("room.id"), primary_key=True),
)
