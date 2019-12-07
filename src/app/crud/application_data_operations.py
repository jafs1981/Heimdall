from sqlalchemy.orm import Session
from app import schemas, models
import uuid


def get_application_by_id(db: Session, application_id: uuid.UUID):
    return db.query(models.IsxApplication)\
        .filter(models.IsxApplication.application_id == str(application_id))\
        .first()


# ---------------------------------------------------------------------------------------
# POST APPLICATIONS
# ---------------------------------------------------------------------------------------
def get_applications(db: Session, skip: int = 0, limit: int = 100, **kwargs):
    query = db.query(models.IsxApplication)
    if 'is_enabled' in kwargs and kwargs.get('is_enabled') is not None:
        enabled = False
        if kwargs.get('is_enabled').lower() == 'true':
            enabled = True
        query = query.filter(
            models.IsxApplication.is_enabled == enabled
        )
    return query.offset(skip).limit(limit).all()
