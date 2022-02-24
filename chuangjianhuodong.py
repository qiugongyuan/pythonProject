import pymysql
import time
import datetime

conn = pymysql.connect(
    host='47.97.36.223',
    user='smt001',
    passwd='4a70079332c44f58',
    db='momtime_eshop',
    port=33006,
    charset='utf8'
)
t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
t2 = '2022-02-24 23:59:59'
tns = datetime.datetime.now()
print(tns)
cur = conn.cursor()
count = 1
while count < 3:
    count += 1
    activity_name = '测试活动' + str(count)
    sql = '''INSERT INTO lottery_activities(`activity_name`, `start_date`, `end_date`,`activity_targets`, `limt`, `rule_of_get`, `the_goods`, `award_provider_type`, `awards`,`days_after`, `remark`,`detail`,`lottery_status`,`create_time`,`to_target`,`banner`,`activity_img`,`background_colour`,`background_img`,`button_img`,`button_colour`) \
          VALUES (\"{}\", \"{}\", \"{}\", \"{}\","0", \"{}\", \"{}\", "3", \"{}\", "0", \"{}\", \"{}\", \"{}\", \"{}\","1","https://momtime-manage.oss-cn-hangzhou.aliyuncs.com/image/2022/2/21/579f64268a9044e68bf2a083d017f672.jpg","https://momtime-manage.oss-cn-hangzhou.aliyuncs.com/image/2022/2/21/3d2a60ae85fa44eda01830b730deda0b.png","#FB5849","https://momtime-manage.oss-cn-hangzhou.aliyuncs.com/image/2022/2/21/d0944bf3a44945bdb8552c98046c05f6.png","https://momtime-manage.oss-cn-hangzhou.aliyuncs.com/image/2022/2/21/e52329821ecb41cda258c1246fea2429.png","#FB5849");'''.format(
        activity_name, t, t2, \
        "[]", "{\\\"RullOfGet\\\":1,\\\"Limt\\\":0}", "[{\\\"GoodsName\\\":\\\"test\\\"}]",
        "[{\\\"AwardLevel\\\":1,\\\"AwardName\\\":\\\"啊手动阀\\\",\\\"AwardImage\\\":\\\" \\\",\\\"AwardProvider\\\":1,\\\"Rate\\\":0},{\\\"AwardLevel\\\":2,\\\"AwardName\\\":\\\"爱的色放\\\",\\\"AwardImage\\\":\\\" \\\",\\\"AwardProvider\\\":2,\\\"Rate\\\":50},{\\\"AwardLevel\\\":3,\\\"AwardName\\\":\\\"啊手动阀\\\",\\\"AwardImage\\\":\\\" \\\",\\\"AwardProvider\\\":2,\\\"Rate\\\":50}]",
        "活动简介:qq", "<p>啊手动阀</p>", "2", tns)
    cur.execute(sql)
    conn.commit()
    print('数字' + str(count))
print("已经插入完成")
cur.close()
conn.close()
