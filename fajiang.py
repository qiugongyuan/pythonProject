import codecs
import json

import requests

source = codecs.open("E:\\testfile\\performance\\fajiang.txt", "r", "gb18030")
values = source.readlines()
phones = []
users = []

for val in values:
    phone, user = val.split(',')
    phone = phone.strip('\t\r\n')
    user = user.strip('\t\r\n')
    phones.append(phone)
    users.append(user)
print(phones)
print(users)

headers = {
 "token" :"5d4d1f8413954b0da2a11082f9e612c5",
 "User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 15_2_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.18(0x1800122c) NetType/WIFI Language/zh_CN",
 "Accept-Encoding":"gzip",
 "Accept-Language":"zh-CN,zh;q=0.9",
 "Content-Type":"application/json",
 "Content-Length":"129",
}
for phone in phones:

        data={
           "codeCount":"20",
           "theGoods":
               [{"goodsName":"test","count":1}],
           "totalMoney":"120",
           "lotteryActivityId":54,
           "phone":phone

        }
        url = "https://platform-test-api.momtime.com/app/lotteryActivity/randomAwardSend"
        luckyUrl = requests.post(url=url, data=json.dumps(data),headers=headers)
        with open('C:/Users/Lenovo/Desktop/choujiang/choujiang.txt', 'a+', encoding='utf-8') as f:
             print(luckyUrl.text, file=f)
             print('--------------------\n', file=f)
             print(luckyUrl)
