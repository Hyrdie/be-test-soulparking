import uvicorn
from fastapi import FastAPI
from settings import settings
from fastapi.middleware.cors import CORSMiddleware
import logging
from api.todo_api import todo_api

app = FastAPI(title=settings.APP_NAME)

logger = logging.basicConfig(filename=settings.LOG_FILE)
logger = logging.getLogger(settings.GET_LOGGER)
logger.setLevel(settings.LOG_LEVEL)

origins = settings.ORIGINS

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=settings.CORS_ALLOW_METHODS,
    allow_headers=settings.CORS_ALLOW_HEADERS
)

@app.get("/alive")
async def getInfo():
    return {
        "desc":"Microservices for todolist-rest-api"
    }

@app.on_event("startup")
async def startup():
    logger.info("todolist-rest-api service is up!!!")

@app.on_event("shutdown")
async def shutdown():
    logger.info("shutting down todolist-rest-api service...")

app.include_router(todo_api, tags=["list of all todo api"])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)