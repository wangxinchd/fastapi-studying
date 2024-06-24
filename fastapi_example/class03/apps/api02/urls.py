from fastapi import APIRouter

app02 = APIRouter()


# 模拟查询数据
#   'http://127.0.0.1:8000/app02/jobs/python?xl=%E6%9C%AC%E7%A7%91&gj=3-5%E5%B9%B4'

@app02.get('/jobs/{kd}')
async def get_jobs(kd, xl, gj):  # kd: 职位关键词, xl: 学历要求, gj: 工作经验
    return {
        "kd": kd,
        "xl": xl,
        "gj": gj
    }


#   'http://127.0.0.1:8000/app02/jobs_2/?kd=python&xl=%E6%9C%AC%E7%A7%91&gj=3' 
@app02.get('/jobs_2/')
async def get_job_2(kd, xl, gj):  # kd: 职位关键词, xl: 学历要求, gj: 工作经验
    return {
        "kd": kd,
        "xl": xl,
        "gj": gj
    }