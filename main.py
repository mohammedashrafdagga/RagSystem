from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv(".env")

# calling routers
from routers import base
import uvicorn

# loading env


# init the application
app = FastAPI()


# register the routers
app.include_router(base.base_app)


# run the application
if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
