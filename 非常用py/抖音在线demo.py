from appium import webdriver
import time
import xlwt, xlrd
workbook = xlwt.Workbook(encoding='utf-8')# 创建一个workbook 设置编码
worksheet = workbook.add_sheet('My Worksheet')# 创建一个worksheet
desired_caps = {
            "platformName": "Android",
            "deviceName": "MHA_AL00",
            "appPackage": "com.ss.android.ugc.aweme",
            "appActivity": ".main.MainActivity",
            "noReset": "true",
            "fullReset": "false"
}
server = 'http://localhost:4723/wd/hub'
driver = webdriver.Remote(server, desired_caps)
time.sleep(3)
#driver.tap([(710, 2100),(780, 2400)],100)
driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "消息")]').click()
time.sleep(1)
driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "")]').click()
time.sleep(1)
while True:
    status=driver.find_element_by_id('com.ss.android.ugc.aweme:id/blc').text
    strtime = time.strftime("%H:%M:%S", time.localtime(time.time()))
    if status=='在线':
        status='在线'
    else:
        status='不在线'
    wb = xlrd.open_workbook('1.xls')
    tabsheet = wb.sheets()[0]
    k = tabsheet.nrows  # 表格已有的行数
    worksheet.write(k , 0, strtime)  # 时间
    worksheet.write(k , 1, status)  # 在线状态
    workbook.save('1.xls')
    time.sleep(60)


    #需要修改其中参数，现在还未成功！