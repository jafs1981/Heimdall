from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table, Date, Float, Text, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.schema import PrimaryKeyConstraint, ForeignKeyConstraint
from .database import Base
import uuid
import datetime


def _generate_id():
    return uuid.uuid4()


def _get_date():
    return datetime.datetime.now()


# -----------------------------------------------------------------------------
# TABLE ISX Application
# -----------------------------------------------------------------------------
class IsxApplication(Base):

    __tablename__: str = 'isx_application'

    application_id = Column(UUID, primary_key=True, index=True)
    name = Column(String(40), nullable=False)
    description = Column(String(256))
    callback_url = Column(String(4000), nullable=False)
    public_key = Column(String(2048), nullable=False)
    private_key = Column(String(4096), nullable=False)
    environment = Column(String(50), nullable=False)
    configuration = Column(JSONB(astext_type=Text()))
    last_modified = Column(DateTime)
    is_enabled = Column(Boolean, index=True)


# -----------------------------------------------------------------------------
# ISX CLAIMS PROVIDER
# -----------------------------------------------------------------------------
class IsxClaimsProvider(Base):
    __tablename__ = 'isx_claims_provider'

    provider_id = Column(UUID, primary_key=True)
    name = Column(String(40), nullable=False)
    description = Column(String(256))
    is_local = Column(Boolean)
    config = Column(JSONB(astext_type=Text()))
    implementation_class = Column(String(200), nullable=False)
    credentials = Column(JSONB(astext_type=Text()))


