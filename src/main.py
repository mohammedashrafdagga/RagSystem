from fastapi import FastAPI


# calling routers
from routers import base, data
import uvicorn

# loading env


# init the application
app = FastAPI()


# register the routers
app.include_router(base.base_app)
app.include_router(data.data_app)

# run the application
if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
