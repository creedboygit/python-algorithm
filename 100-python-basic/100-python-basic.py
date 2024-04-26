# 정수형
print("===========")
a = 1
b = 2
c = -11

print(a, b, c)  # 1 2 -11

# 실수형
print("===========")
a = 1.23
b = 3.
c = -13.2

print(a, b, c)  # 1.23 3.0 -13.2

# 지수형
print("===========")
d = 1e4
e = 3000e-2

print(d, e)  # 10000.0 30.0

print("===========")
a = 0.3 + 0.6

print(a, round(a))

# 연산
print("===========")
a = 2
b = 2

print(a / b)  # 0.5
print(a % b)  # 1
print(a // b)  # 0
print(a ** b)  # 1

# 리스트
print("===========")
a = [1, 2, 3, 4]
print(a)  # [1, 2, 3, 4]

# 리스트 - 인덱싱, 슬라이싱
print("===========")
a = [1, 2, 3, 4]

# 인덱싱
print(a[0])  # 1
print(a[-1])  # 4
print(a[-2])  # 3

# 변경
a[3] = 5
print(a)  # [1, 2, 3, 5]

# 슬라이싱
print(a[1:3])  # [2, 3]
print(a[:-1])  # [1, 2, 3]
print(a[1:-1])  # [2, 3]

# 리스트 컴프리헨션 (list comprehension)

# 1차원 리스트 초기화
print("===========")
a = [0] * 5
print(a)  # [0, 0, 0, 0, 0]

# 2차원 리스트 초기화
a = [[0] * 5 for _ in range(3)]
print(a)  # [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

# 1 ~ 9 중 홀수인 제곱수 리스트
a = [i ** 2 for i in range(1, 10) if i % 2 == 1]
print(a)

# 리스트 메서드
print("===========")

a = [2, 3, 4]

# 추가
a.append(1)
print(a)  # [2, 3, 4, 1]

# 정렬
a.sort()
print(a)  # 오름차순 [1, 2, 3, 4]

a.sort(reverse=True)
print(a)  # 내림차순 [4, 3, 2, 1]

a.reverse()  # 뒤집기 1
print(a)

a.reverse()  # 뒤집기 2
print(a)

a.reverse()  # 뒤집기 3
print(a)

# 삽입 (idx, value)
a.insert(1, 2)  # [1, 2, 2, 3, 4]
print(a)

# 개수
print(a.count(2))  # 2 (배열에서 x의 개수)

# 값으로 제거 (앞에서 가장 먼저 나오는 하나만 제거)
a.remove(2)
print(a)

# 값으로 제거 (앞에서 가장 먼저 나오는 하나만 제거)
# a.remove(10)
# print(a)

# 인덱스 번호로 제거
print(a.pop(2))
print(a)

# 문자열 자료형 (String)
# 선언
print("===========")

a = 'Hi'
print(a)  # Hi

# 연산
b = 'Bye'
print(a + " " + b)  # Hi Bye

# 반복
print(a * 3)  # HiHiHi

# 슬라이싱
print(b[1:3])  # ye

# 튜플 자료형 (Tuple)
# 선언
print("===========")
a = (1, 2, 3, 4)
print(a)  # (1, 2, 3, 4)

# 선언 후 변경 불가
# a[2] = 3  # 'tuple' object does not support item assignment

# 딕셔너리 자료형 (Dictionary)
# key: value 쌍
data = {}
data['a'] = 'aaa'  # {'a': 'aaa'}
data['b'] = 'bbb'  # {'a': 'aaa', 'b': 'bbb'}
print("===========")
print(data)

# key
print("===========")
print(data.keys())  # dict_keys(['a', 'b'])

# value
print("===========")
print(data.values())  # dict_values(['aaa', 'bbb'])

# Set 자료형
# 중복 불가, 순서 없음
print("===========")
data = set([1, 1, 2])
print(data)  # {1, 2}

data = {1, 1, 2}
print(data)

# 연산
a = {1, 2, 3}
b = {3, 4, 5}

# 합집합
print("===========")
print(a | b)  # {1, 2, 3, 4, 5}

# 교집합
print(a & b)  # {3}

# 차집합
print(a - b)  # {1, 2}

# 메서드
a = {1, 2, 3}

# 추가
a.add(4)  # {1, 2, 3, 4}
print("===========")
print(a)

# 여러 개 추가
a.update([5, 6])  # {1, 2, 3, 4, 5, 6}

print("===========")
print(a)

# 삭제
a.remove(3)  # {1, 2, 4, 5, 6}
print(a)