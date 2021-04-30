#   -*- coding:'utf-8' -*-
import threading
import requests

while True:
    city = input("请输入城市，回车退出：\n")
    if not city:
        break

    try:
        #requests.get()　获取HTML网页的主要方法，对应于HTTP的GET
        req = requests.get('http://wthrcdn.etouch.cn/weather_mini?city=%s'%city)
    except:
        print('查询失败！')
        break

    # print(req.text)
    dir_city = req.json()   #可以将数据直接输出为字典
    print(dir_city) #一定要将这一句话先输出查看字典里面的内容，以便于更好地理解下面的操作
    print(type(dir_city))   #为字典
    city_data = dir_city.get('data')    #没有 ‘data’的话返回None

    if city_data:
        city_forecast = city_data['forecast'][1]    #
        print(type(city_forecast))
        print(city_forecast.get('date'))
        print(city_forecast.get('high'))
        print(city_forecast.get('low'))
        print(city_forecast.get('type'))
    else:
        print("未获得！")


def get_weather(city):
    req = requests.get('http://wthrcdn.etouch.cn/weather_mini?city=%s' % city)
    dic_city = req.json()

    city_data = dic_city.get('data')  # 没有’data‘的话返回 []
    print(city_data.get('city'))

    if city_data:
        city_forecast = city_data['forecast'][0]  # 下面的都可以换成'get'方法
        print(city_forecast.get('date'))
        print(city_forecast.get('high'))
        print(city_forecast.get('low'))
        print(city_forecast.get('type'))
    else:
        print('未获得')
    print()


# 针对每一个城市，都创建了一个新线程，并将线程加入到一个列表中，用于之后的启动。

threads = []
cities = ['北京', '南京', '上海', '深圳', '广州', '杭州', '苏州', '天津', '西安', '成都']
files = range(len(cities))
for i in files:  # 创建线程
    t = threading.Thread(target=get_weather, args=(cities[i],))
    threads.append(t)

# 在第二个循环中，start
# 正式开启子线程；

for i in files:
    threads[i].start()

# 在第三个循环中，join
# 用来同步数据，主线程运行到这一步，将会停下来等待子线程运行完毕。没有这句，主线程则会忽略子线程，运行完自己的代码后结束程序。

for i in files:
    threads[i].join()
