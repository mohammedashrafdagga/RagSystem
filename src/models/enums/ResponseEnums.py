from enum import Enum


class ResponseSignal(Enum):
    FILE_VALIDATE_SUCCESSfULLY = "file validate successfully"
    FILE_TYPE_NOT_SUPPORTED: str = "file_type not supported"
    FILE_SIZE_EXCEEDED = "file size exceeded"
    FILE_UPLOADED_SUCCESS: str = "file uploaded success"
    FILE_UPLOADED_FAILED: str = "file uploaded failed"
