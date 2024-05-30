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

# format 함수처럼 string 자료형 클래스의 멤버함수들이 있습니다.
# .format()
# .count()
# .find()
# .upper()
# .lower()
# .replace()
# .split()
# .isspace()

print('count: ', g.count('기'))
print(g.find('대한민국'))
print(g.replace('대한민국', '미국'))

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

# timedelta - days, seconds, microseconds, milliseconds, minutes, hours, weeks......
yesterdaydt = datetime.datetime.now() - datetime.timedelta(days=1)
print(yesterdaydt)

list1 = ['김치', 0.23, 101, 'abc', [0, 2, 3]]
print("===========")
print(list1)

# 리스트 함수
# append(): 리스트의 끝에 추가
# insert(): 특정 index 에 추가
# extend(): 리스트의 끝에 다른 리스트를 추가
# index(): 특정 값을 가진 첫번째 요소 의 index 를 반환
# pop(): 특정 위치의 요소를 삭제
# remove(): 특정 값을 가진 요소를 삭제
# clear(): 모든 요소 삭제
# count(): 특정 값을 가진 요소의 수를 반환
# sort(): 정렬

# 딕셔너리
dict = {'email': 'a@gmail.com', 'age': 19, 'tel': '010-3020-3020', 'weight': 56}
print("===========")
print(dict)

print(dict.keys())

print(dict.values())

dict['tall'] = 164

print(dict)


# print()	출력
# input()	입력
# range()	정수의 범위 설정하고 배열로 만듬
# list()	리스트 생성
# abs()	부호를 + 로 변경
# len()	길이
# round()	소수점 이하 반올림
# int()	int 정수형으로 변경
# float()	float 실수형으로 변경
# str()	문자열로 변경
# type()	데이터 또는 클래스의 형을 반환
# id()	변수, 함수, 클래스 등의 인스턴스의 메모리 주소를 나타내는 고유 id

# 전역 변수
def foo():
    global x
    print(x)

x = 10
print("===========")
print(x)
x += 100
foo()


# 클래스
class className:
    def __init__(self):
        self.name = 'class1'

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

print("===========")
c1 = className()
c1.set_name('이름이름')
print(c1.get_name())
print(c1.name)
