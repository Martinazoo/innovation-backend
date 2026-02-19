import uuid
from sqlalchemy import Column, Integer, Boolean, TIMESTAMP, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from database import Base

class TempCheckpointDB(Base):
    __tablename__ = "tempCheckpoint"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    order_num = Column(Integer)
    scanned = Column(Boolean)
    scanTimeframe = Column(TIMESTAMP)

    checkpoint_id = Column(
        UUID(as_uuid=True),
        ForeignKey("checkpoint.id"),
        nullable=False
    )

    tempRoute_id = Column(
        UUID(as_uuid=True),
        ForeignKey("tempRoute.id"),
        nullable=False
    )

    checkpoint = relationship("CheckpointDB", back_populates="temp_checkpoints")
    temp_route = relationship("TempRouteDB", back_populates="temp_checkpoints")