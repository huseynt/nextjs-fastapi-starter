from fastapi import FastAPI
app = FastAPI(docs_url="/api/py/docs", openapi_url="/api/py/openapi.json")



@app.get("/")
def read_root():
    return {"message": "hello !"}


@app.get("/api/hello")
def hello_fast_api():
    return {"message": "Hello from FastAPI"}

@app.get("/api/py/helloFastApi/{name}")
def hello_fast_api_name(name: str):
    return {"message": f"Hello {name} from FastAPI"}

@app.post("/api/predict")
def hello_fast_api_post(body: dict, headers: dict):
    return {"message": "Hello from FastAPI POST", "body": body, "headers": headers}
