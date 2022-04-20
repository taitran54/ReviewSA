from fastapi import FastAPI, Request
from fastapi.middleware.core import CORSMiddleware
from typing import Optional
import time, asyncio


from .modules.sentiment import predict_data
from .routers import review
app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
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
    print(await list_test.json())
    return { "Message" : "Test done" }

@app.get("/")
async def root():
    # return {"Message" : "This is an instruction",
    #         "Function" : "Predict stars of review",
    #         "Route" : "/reviewsa",
    #         "Full_link" : "https://reviewsafastapi.et.r.appspot.com/reviewsa",
    #         "Method" : "GET",
    #         "Query_params" : 
    #             { "sentence" : 
    #                 { "type" : "String", 
    #                   "note" : "Your review which need to predict"} } }
    return { "Message" : "Hello World" }