from typing import List, Dict
import uuid
from datetime import datetime
from pydantic import Schema, BaseModel


class Application(BaseModel):

    application_id: uuid.UUID = Schema(None, title="Unique identifier for a given application")
    name: str = Schema(None, title="Application name", max_length=40)
    description: str = Schema(None, title="Application description", max_length=256)
    callback_url: str = Schema(None, title="Callback URL where access token is returned after authorization", max_length=4000)
    public_key: str = Schema(None, title="Public Cryptographic Key used to validate JWT Signatures", max_length=4096)
    private_key: str = Schema(None, title="Private Cryptographic Key used to validate JWT Signatures", max_length=4096)
    environment: str = Schema(
        None, title="Tag that describes the application's environment (Ex: Dev, Test, Prod)", max_length=50
    )
    configuration: dict = Schema(None, title="Additional configurations for the application")
    last_modified: datetime = Schema(
        None, title="Time stamp of the last modification made to the application definition"
    )
    is_enabled: bool = Schema(
        None, title='If the application is enabled of not to authorize users'
    )