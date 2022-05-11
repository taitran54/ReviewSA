from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
import time, asyncio

from .modules.lstmmodel import predict_data
from .routers import review

app = FastAPI()

origins = [
    "https://nongsanmietvuon.herokuapp.com",
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(review.router)

@app.get("/test")
async def test(list_test : Request):
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(predict_data(["Món này rất ngon"]))
    # await predict_data(["Món này rất ngon"])
    x = await predict_data(['Món này ngon quá'])
    print (x)
    # print(await list_test.json())
    return { "Message" : "Test done" }

@app.get("/")
async def root():
    try: 
        result = { "Message" : "This is a main route" }
    
    except:
        result = { "Message" : "Wrong prototype" }
    finally:
        return result