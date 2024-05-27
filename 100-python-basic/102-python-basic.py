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