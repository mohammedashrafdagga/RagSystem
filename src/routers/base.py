from fastapi import FastAPI, APIRouter, Depends
from helpers.config import get_settings, Settings

# base App
base_app = APIRouter(prefix="/api/v1", tags=["BaseApplication"])


# call from api
@base_app.get("/")
async def welcome(app_settings: Settings = Depends(get_settings)):
    app_name = app_settings.APP_NAME
    app_version = app_settings.APP_VERSION
    return {"app_name": app_name, "app_version": app_version}
