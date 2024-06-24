from fastapi import APIRouter

app01 = APIRouter()

@app01.get("/user/1")
async def get_user():
    return {"user_id": "1234"}

@app01.get("/user/{user_id}")
async def get_user(user_id: int):
    print(f"Getting user with id {user_id}")
    return {"user_id": user_id}