import requests
from datetime import datetime, timedelta

# 访问get quary的案例
api_prefix = "url地址"

def get_stat_day_by_date(date: str):
    ret = requests.get(
        f"{api_prefix}/api/stat/statday",
        params={
            "date": date,
        },
        timeout=10,
    )
    return ret.json()


data = get_stat_day_by_date("2024-06-24")
if data:
    print("Received data:", data)

i = 1
current_date = datetime.now().date()
while True:
    if i > 10:
        print("Failed to get data for 10 days, exit.")
        break

    tmp_date = current_date - timedelta(days=i)
    tmp_date_str = tmp_date.strftime("%Y-%m-%d")

    tmp_date_data = get_stat_day_by_date(tmp_date_str)
    if len(tmp_date_data) == 0:
        i+=1
        continue
    else:
        break

print("Received data:0000", tmp_date_data)


