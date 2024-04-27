from fastapi import FastAPI
from routers import anturit
from routers import lohko
from routers import mittatulos
from database.database import create_db
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db()
    yield
#FastApi app instance
app = FastAPI(lifespan=lifespan)
app.include_router(anturit.router)
app.include_router(lohko.router)
app.include_router(mittatulos.router)