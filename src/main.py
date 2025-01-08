from fastapi import FastAPI

from motor.motor_asyncio import AsyncIOMotorClient
from helpers.config import get_settings

# calling routers
from routers import base, data
import uvicorn

# loading env


# init the application
app = FastAPI()


# when every startup
@app.on_event("startup")
async def startup_db_client():
    settings = get_settings()
    app.mongo_conn = AsyncIOMotorClient(settings.MONGODB_URI)
    app.db_client = app.mongo_conn[settings.MONGODB_DATABASE_NAME]


# close connection when close app
@app.on_event("shutdown")
async def shutdown_db_client():
    app.mongo_conn.close()


# register the routers
app.include_router(base.base_app)
app.include_router(data.data_app)

# run the application
if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
