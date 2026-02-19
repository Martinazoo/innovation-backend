import uuid
from sqlalchemy import Column, Float, String, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from database import Base

class TempRouteDB(Base):
    __tablename__ = "tempRoute"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    posX = Column(Float)
    posY = Column(Float)
    status = Column(String(255))
    startTimeframe = Column(TIMESTAMP)
    endTimeframe = Column(TIMESTAMP)

    temp_checkpoints = relationship("TempCheckpointDB", back_populates="temp_route")
