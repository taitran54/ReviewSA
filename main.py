from fastapi import FastAPI
# from joblib import load
# from underthesea import word_tokenize

app = FastAPI()

@app.get("/")
async def root():
    return {"message" : "Hello Uyên"}