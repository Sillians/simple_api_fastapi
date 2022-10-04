import json
import uvicorn
from fastapi import FastAPI
from core import config
from data.fruits import get_fruits_data
from data.new_data import get_new_data
from data.new_fruits import get_new_fruits_data

import logging
log = logging.getLogger(__name__)

app = FastAPI(title=config.PROJECT_NAME, version=config.VERSION)

fruits_data_json = get_fruits_data()
new_data_json = get_new_data()
new_data_fruits_json = get_new_fruits_data()


@app.get("/")
async def root():
    return {"message": "Hello Sillians World of learning and building awesome APIs..."}


@app.get("/new_data")
async def get_new_data():
    return {"new_data": new_data_json}


@app.get("/fruits")
async def get_data_fruits():
    return {"fruits": fruits_data_json}


@app.get("/fruits/{fruit_id}")
async def get_fruit(fruit_id: int):
    fruit_ = fruits_data_json['fruits'][fruit_id]
    return {"fruit_details": fruit_}


@app.get("/new_fruits")
async def get_new_data_fruits():
    return {"new_fruits": new_data_fruits_json}


@app.get("/new_fruits/{fruit_name}")
async def get_new_fruit_details(fruit_name: str):
    new_frui = [fruit for fruit in new_data_fruits_json if fruit['name'] == fruit_name]
    return {"new_fruit_details": new_frui}


def main():
    log.info("Starting Sillians API Endpoint")
    uvicorn.run("server:app", host="0.0.0.0", port=8001, reload=True, workers=2)


if __name__ == "__main__":
    main()
