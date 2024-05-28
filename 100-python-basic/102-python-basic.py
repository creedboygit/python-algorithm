# 인덱스 추출
val = 'hello valletta!'
print(val[:])
print(val[0:3])
print(val[3:])
print(val[:2])
print(val[-1])
print(val[-3:])
print(val[-4:-2])

# 문자열 포맷팅
sam = '샘'
a = '안녕하세요 %s' % sam
print("===========")
print(a)

today = 3
b = '오늘은 %d 일입니다' % today
print(b)

pi = 3.14
c = '파이는 %d ' % pi
print(c)

# d = '%d'
d = '%d-%02d-%02d' % (2022, 4, 2)
print("===========")
print(d)

f = '%.4f' % pi
print(f)

g = '여기는 {} {} {} 입니다'.format('대한민국', '서울시', '강남구')
print(g)

# 날짜 시간 클래스 라이브러리
import datetime
print("===========")
print(datetime.datetime.now())
print(datetime.datetime.today())

timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
print(timestamp)
print(type(timestamp))

dt = datetime.datetime.strptime(timestamp, "%Y%m%d-%H%M%S")
print(f"dt: {dt}")
print(type(dt))

# timedelta - days, seconds, microseconds, milliseconds, minutes, hours, weeks..
yesterdaydt = datetime.datetime.now() - datetime.timedelta(days=1)
print(yesterdaydt)