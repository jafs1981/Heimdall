from fastapi import FastAPI
from .routers import sample, employee, knowledge_source, knowledge_source_type, role, skill_component
from starlette.middleware.cors import CORSMiddleware
from . import models
from .database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)

# -----------------------------------------------------------------------------
# APPLICATION OBJECT
# -----------------------------------------------------------------------------
app = FastAPI(
    title="Files Microservice",
    description="File management microservice",
    version="1.0.0",
    openapi_url="/file_management/v1/openapi.json",
    docs_url="/file_management/v1/swagger",
    redoc_url="/file_management/v1/docs"
)


# -----------------------------------------------------------------------------
# CORS RULES
# -----------------------------------------------------------------------------
origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------------------------------------------------------
# ADD ROUTERS
# -----------------------------------------------------------------------------
app.include_router(sample.router, prefix="/file_management/v1")


