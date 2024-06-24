from fastapi import FastAPI
import uvicorn
from apps.api01.urls import shop
from apps.api02.urls import user

app = FastAPI()


# 这里的tags 就是docs 网站上面的接口分类
app.include_router(shop, prefix="/shop", tags=["购物中心接口"])
app.include_router(user, prefix="/user", tags=["用户中心接口"])

if __name__ == '__main__':
    uvicorn.run("run:app", port=8000, reload=True)