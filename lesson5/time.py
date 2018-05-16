import time
import datetime

# 获取当前时间戳
tm = time.time()
print(tm)

# 时间戳转换为时间元组
local_time = time.localtime(1231231231)
print(local_time)

print(time.strftime('%Y-%m-%d %H:%M:%S'))
print(time.strftime('%Y-%m-%d %H:%M:%S', local_time))

print(time.strptime('2009-01-06 16:40:31', '%Y-%m-%d %H:%M:%S'))

print(time.mktime(local_time))

tm_b = time.time()
time.sleep(5)
tm_l = time.time()
print(tm_l - tm_b)

print(datetime.datetime.now())

print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

start_time = datetime.datetime.now()
time.sleep(2)
end_time = datetime.datetime.now()
print(end_time - start_time)
print((end_time - start_time).seconds)

ts = time.time()
print(datetime.datetime.fromtimestamp(ts))

today = datetime.datetime.today()
print(today.strftime('%Y-%m-%d'))
timedelta = datetime.timedelta(days=1)
yestoday = today - timedelta
print(yestoday.strftime('%Y-%m-%d'))
