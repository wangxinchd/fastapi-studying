from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to my API"}

@app.get("/shop")
def shop():
    return {"message": "Welcome to my shop"}

if __name__ == "__main__":
    uvicorn.run("fastapi_quickstart:app", port=8080, reload=True)

# fastapi_quickstart[文件名]:app[实例名]
# uvicorn fastapi_quickstart:app --reload         # to run the app in debug mode with hot reload