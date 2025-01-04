# for logic of data routers
from .BaseController import BaseController
from .ProjectController import ProjectController
from fastapi import UploadFile
from models import ResponseSignal
import re
import os


class DataController(BaseController):
    def __init__(self):
        super().__init__()
        self.size_scale = 1048576

    def validate_file_properties(self, file: UploadFile):
        # check type
        if file.content_type not in self.app_settings.FILE_ALLOWED_TYPES:
            return False, ResponseSignal.FILE_TYPE_NOT_SUPPORTED.value

        # check size
        if file.size > self.app_settings.FILE_MAX_SIZE * self.size_scale:
            return False, ResponseSignal.FILE_SIZE_EXCEEDED.value

        return True, ResponseSignal.FILE_VALIDATE_SUCCESSfULLY.value

    # using regex clean file name
    def get_clean_file_name(self, orig_file_name: str):
        clean_file_name = re.sub(r"[^\w.]", "", orig_file_name.strip())
        return clean_file_name.replace(" ", "_")

    def generate_unique_filename(self, orig_file_name: str, project_id: str):
        random_file_name = self.generate_random_string()
        project_dir_path = ProjectController().get_project_path(project_id=project_id)
        clean_file_name = self.get_clean_file_name(orig_file_name=orig_file_name)
        new_file_path = os.path.join(
            project_dir_path, random_file_name + " " + clean_file_name
        )
        # check the name if in project dir path
        while os.path.exists(new_file_path):
            random_file_name = self.generate_random_string()
            new_file_path = os.path.join(
                project_dir_path, random_file_name + " " + clean_file_name
            )

        return new_file_path
