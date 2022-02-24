import json
from pip._vendor import requests
headers = {
 "token" :"022382af574b4fef860c2093deb9843a",
 "User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 15_2_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.18(0x1800122c) NetType/WIFI Language/zh_CN",
 "Accept-Encoding":"gzip",
 "Accept-Language":"zh-CN,zh;q=0.9",
 "Content-Type":"application/json",
 "Content-Length":"129"
}
data={
  "lotteryActivitySendId":"75",
  "openId":"ojxPV5AeIqE38dVRYXv5EvB-S59o",
  "codeCount":1
}
n = 0
while n < 21:
    # 抽奖接口
    url = "https://platform-test-api.momtime.com/platform-eshop/lotteryActivity/randomAward"
    luckyUrl = requests.post(url=url, data=json.dumps(data),headers=headers)
    print(luckyUrl)
    with open('C:/Users/Lenovo/Desktop/choujiang/choujiang.txt', 'a+', encoding='utf-8') as f:
        print(luckyUrl.text, file=f)
        print('--------------------\n', file=f)
    print("这是第"+str(n+1) +"次")
    n+=1
