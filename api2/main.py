from fastapi import FastAPI

app = FastAPI()


@app.get("/uppercase/{text}")
def uppercase(text: str):
    return {"result": text.upper()}


@app.get("/lowercase/{text}")
def lowercase(text: str):
    return {"result": text.lower()}
