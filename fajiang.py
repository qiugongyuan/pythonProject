import json
from pip._vendor import requests
headers = {
 "token" :"97ac5b92e9974398a9ccdf7e54fe8bb8",
 "User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 15_2_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.18(0x1800122c) NetType/WIFI Language/zh_CN",
 "Accept-Encoding":"gzip",
 "Accept-Language":"zh-CN,zh;q=0.9",
 "Content-Type":"application/json",
 "Content-Length":"129",
}
data={
   "codeCount":"20",
   "theGoods":
       [{"goodsName":"test","count":1}],
   "totalMoney":"120",
   "lotteryActivityId":11,
   "phone":"15330235989"
}
n = 0
while n < 5:
    # 抽奖接口
    url = "https://platform-test-api.momtime.com/app/lotteryActivity/randomAwardSend"
    luckyUrl = requests.post(url=url, data=json.dumps(data),headers=headers)
    with open('C:/Users/Lenovo/Desktop/choujiang/choujiang.txt', 'a+', encoding='utf-8') as f:
        print(luckyUrl.text, file=f)
        print('--------------------\n', file=f)
    print("这是第"+str(n+1) +"次")
    n+=1
