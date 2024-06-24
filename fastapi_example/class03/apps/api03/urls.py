from typing import List, Union
from fastapi import APIRouter
from datetime import date
from pydantic import BaseModel, Field, ValidationError, field_validator

app03 = APIRouter()

class User(BaseModel):
    name: str = "root" # default value
    age: int = Field(default=18, gt=0, lt=100) # Field 用于做限制默认值、最小值、最大值
    birth: Union[date, None] = None # 日期类型 填写字段格式：1990-01-01
    friends: list[int]

    @field_validator('name') #装饰器，验证器
    def name_must_contain_space(cls, v): # 函数名无所谓，但必须是类方法 cls: 类名 v: 字段值
        assert v.isalpha(), 'name must be alphabetic' # 断言，必须包含字母
        return v

@app03.post('/data')
async def data(user: User):
    print(user, type(user))
    print(user.model_dump())
    return {'data': user}

"""
{
  "name": "123445",
  "age": 18,
  "birth": "2018-06-16",
  "friends": [
    0
  ]
}

print(user, type(user)) 输出：
name='123445' age=18 birth=datetime.date(2018, 6, 16) friends=[0] <class 'apps.api03.urls.User'>

print(user.model_dump()) 输出：
{'name': '123445', 'age': 18, 'birth': datetime.date(2018, 6, 16), 'friends': [0]}
"""

class Data(BaseModel):  # 类型嵌套 支持输出多个数据
    users: List[User]


@app03.post("/data_02/")
async def create_data(data: Data):
    # 添加数据库
    return data

"""
{
  "users": [
    {
      "name": "root",
      "age": 18,
      "birth": "2024-06-16",
      "friends": [
        0
      ]
    },
    {
      "name": "rootout",
      "age": 18,
      "birth": "2024-03-16",
      "friends": [
        0,123
      ]
    }
  ]
}

"""
