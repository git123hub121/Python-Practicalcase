from appium import webdriver
import time
import aircv as ac
# def matchImg(imgsrc, imgobj, confidencevalue=0.7):  # imgsrc=原始图像，imgobj=待查找的图片
#     imsrc = ac.imread(imgsrc)
#     imgobj = ac.imread(imgobj)
#     match_result = ac.find_template(imsrc, imgobj,confidencevalue)  # {'confidence': 0.5435812473297119, 'rectangle': ((394, 384), (394, 416), (450, 384), (450, 416)), 'result': (422.0, 400.0)}
#     return match_result
desired_caps = {"platformName": "Android",
            "deviceName": "AKA-AL10",
            "appPackage": "com.tencent.mm",
            "appActivity": ".ui.LauncherUI",
            "noReset": "true",
            "fullReset": "false"}
server = 'http://localhost:4723/wd/hub'
driver = webdriver.Remote(server, desired_caps)
time.sleep(5)
# while True:
#     driver.save_screenshot('src.png')
#     imgsrc='src.png'
#     imgobj='obj.png'
#     match_result=matchImg(imgsrc, imgobj)
#     if match_result is not None:
#         result = [match_result['rectangle'][0], match_result['rectangle'][3]]
#         for i in range(2):
#             driver.tap(result,100)
#         print('拍成功')
#     else:
#         print('没找到头像')