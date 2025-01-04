from fastapi import FastAPI, APIRouter, Depends, UploadFile, status
from fastapi.responses import JSONResponse
from helpers.config import get_settings, Settings
from controllers import DataController, ProjectController
from models import ResponseSignal
import os
import aiofiles
import logging

# base App
data_app = APIRouter(prefix="/api/v1/data", tags=["DataApplication"])
logger = logging.getLogger("uvicorn.error")


@data_app.post("/upload/{project_id}")
async def upload_file(
    project_id: str, file: UploadFile, app_settings: Settings = Depends(get_settings)
):
    data_controller = DataController()
    # validate the file properties
    is_valid, result_signal = data_controller.validate_file_properties(file=file)

    if not is_valid:
        return JSONResponse(
            content={"signal": result_signal}, status_code=status.HTTP_400_BAD_REQUEST
        )

    project_dir_path = ProjectController().get_project_path(project_id=project_id)
    file_path = data_controller.generate_unique_filename(
        orig_file_name=file.filename, project_id=project_id
    )

    try:
        async with aiofiles.open(file_path, "wb") as f:
            while chunk := await file.read(app_settings.FILE_DEFAULT_CHUNK_SIZE):
                await f.write(chunk)
    except Exception as e:
        logger.error(f"error while uploading file: {str(e)}")

        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"signal": ResponseSignal.FILE_UPLOADED_FAILED.value},
        )
    # saving the file also
    return JSONResponse(content={"signal": ResponseSignal.FILE_UPLOADED_SUCCESS.value})
