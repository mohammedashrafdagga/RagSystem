from .BaseController import BaseController
from .ProjectController import ProjectController
from langchain_community.document_loaders import TextLoader, PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os
from models import ProcessingEnums


class ProcessController(BaseController):
    def __init__(self, project_id: str):
        super().__init__()
        self.project_id = project_id

        self.project_dir = ProjectController().get_project_path(
            project_id=self.project_id
        )

    # get file extension
    def get_file_extension(self, file_id: str):
        return os.path.splitext(file_id)[-1]

    # get file loader
    def get_file_loader(self, file_id: str):

        file_extension = self.get_file_extension(file_id)
        file_path = os.path.join(self.project_dir, file_id)
        if file_extension == ProcessingEnums.TXT.value:
            return TextLoader(file_path, encoding="utf-8")
        elif file_extension == ProcessingEnums.PDF.value:
            return PyMuPDFLoader(file_path)
        else:
            return None

    # get file content
    def get_file_content(self, file_id: str):
        loader = self.get_file_loader(file_id=file_id)
        # Document (page_content, metadata = {info for file source, page, ids , and ...})
        return loader.load()

    def process_file_content(
        self, file_content: list, file_id: str, chunk_size: int, overlap_size: int
    ):
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=overlap_size,
            length_function=len,
            is_separator_regex=False,
        )
        file_content_texts = [file.page_content for file in file_content]
        file_content_metadata = [file.metadata for file in file_content]

        chunks = text_splitter.create_documents(
            file_content_texts, metadatas=file_content_metadata
        )

        return chunks
