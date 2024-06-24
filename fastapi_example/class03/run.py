from fastapi import FastAPI
import uvicorn
from apps.api01.urls import app01
from apps.api02.urls import app02
from apps.api03.urls import app03
# from apps.api02.urls import user

app = FastAPI()


# 这里的tags 就是docs 网站上面的接口分类
app.include_router(app01, prefix="/app01", tags=["app01"])
app.include_router(app02, prefix="/app02", tags=["app02"])
app.include_router(app03, prefix="/app03", tags=["app03"])

if __name__ == '__main__':
    uvicorn.run("run:app", port=8000, reload=True)