while True:
    year =int(input("请输入年份："))
    month=int(input("请输入月份："))
    day=int(input("请输入日期："))
    sum_day=0                  #表示当前日期是全年的哪一天
    total_month=(31,28,31,30,31,30,31,31,30,31,30,31)  #平年12个月的天数组成放元组
    print(total_month[:month-1])
    sum_day=sum(total_month[:month-1])+day             #总天数=之前所有月份的天数+当前日期的天数
    percent_day=(sum_day/365)*100                      #计算天数占全年365天的百分比
    if year%400==0 or (year%4==0 and year%100!=0):     #如果是闰年
        if month>2:                                    #输入月份大于2月
            sum_day+=1                                 #天数加1
        percent_day=(sum_day/366)*100                  #闰年，全年总天数是366天
    percent_day=round(percent_day,3)                   #保留3位小数
    print(f"{year}年{month}月{day}日是{year}年的第{sum_day}天，全年已经过去了{percent_day}%")
    '''输出*年*月*日是*年的第*天，全年已经过去*%'''
