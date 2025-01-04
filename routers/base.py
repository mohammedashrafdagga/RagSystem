from fastapi import FastAPI, APIRouter
import os

# base App
base_app = APIRouter(prefix="/api/v1", tags=["BaseApplication"])


# call from api
@base_app.get("/")
async def welcome():
    app_name = os.getenv("APP_NAME")
    app_version = os.getenv("APP_VERSION")
    return {"app_name": app_name, "app_version": app_version}
