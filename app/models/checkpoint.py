import uuid
from sqlalchemy import Column, String, Float, Text
from sqlalchemy.dialects.postgresql import UUID, DOUBLE_PRECISION
from sqlalchemy.orm import relationship
from database import Base

class CheckpointDB(Base):
    __tablename__ = "checkpoint"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(255))
    posX = Column(Float)
    posY = Column(Float)
    NFCtag = Column(UUID(as_uuid=True))
    description = Column(Text)
    radius = Column(DOUBLE_PRECISION)

    temp_checkpoints = relationship("TempCheckpointDB", back_populates="checkpoint")
