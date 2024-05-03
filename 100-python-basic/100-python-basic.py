# 정수형
import heapq

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

# 조건문
# if con:
# elif con:
# else:

var = 1 in [1, 2, 3]  # True
print("===========")
print(var)

var = 4 not in [1, 2, 3]  # True
print(var)


# 반복문
# while
# while con:

# for
# for var in list:

# 함수
def add(a, b):
    return a + b


result = add(1, 2)
print("===========")
print(result)

# lambda
add = lambda a, b: a + b
result = add(1, 2)
print(result)

# 입출력
# 개수
# n = int(input())
# n = int(input("입력해주세요. >>> "))

# 데이터
# data = list(map(int, input().split()))
print(f"data: {data}")

# readline 사용 시
import sys

# data = sys.stdin.readline().rstrip()
print(f"data2: {data}")

# 주요 라이브러리
# 내장함수

# 합
result = sum([1, 2, 3])
print("===========")
print(result)

# 최소값, 최대값
print(min(1, 2, 3))  # 1
print(max(1, 2, 3))  # 3

# 문자열 > 수식
print(eval("3 + 5"))  # 8

# key 정렬
# result = sorted([('디', 5), ('비', 1), ('씨', 3)], key=lambda x: x[0])
result = sorted([('디', 5), ('비', 1), ('씨', 3)], key=lambda x: x[1])
print("===========")
print(result)

# itertools - 순열, 조합
# 순열
from itertools import permutations

a = ['A', 'B', 'C']
res = list(permutations(a, 3))
print("===========")
print(res)
# [('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]

# 조합
from itertools import combinations

a = ['A', 'B', 'C']
res = list(combinations(a, 2))
print("===========")
print(res)
# [('A', 'B'), ('A', 'C'), ('B', 'C')]

# 중복순열
from itertools import product

a = ['A', 'B', 'C']
res = list(product(a, repeat=2))
print("===========")
print(res)
# [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]

# 중복조합
from itertools import combinations_with_replacement

a = ['A', 'B', 'C']
res = list(combinations_with_replacement(a, 2))
print(res)
# [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]


# heapq - 힙, 우선순위류
# 파이썬의 힙은 최소힙으로 구성되어 있어서, 원소 전체를 힙에 넣었다 빼는 것만으로 오름차순 정렬이 완료됨 - O(NlogN)

# 추가
# heapq.heappush()

# 제거
# heapq.heappop()

# 정렬
import heapq


def heapsort(iterable):
    h = []
    res = []

    for value in iterable:
        # heapq.heappush(h, value)  # 내림차순 : (h, -value)
        heapq.heappush(h, -value)  # 내림차순 : (h, -value)

    for i in range(len(h)):
        # res.append(heapq.heappop(h))  # 내림차순 : (-heapq.heappop(h))
        res.append(-heapq.heappop(h))  # 내림차순 : (-heapq.heappop(h))

    return res


res = heapsort([1, 3, 5, 7, 9, 2, 4, 6])
print("===========")
print(res)

# bisect - 이진 탐색
# 이진탐색 - 정렬된 배열에서 효과적으로 사용 가능
# 배열 a에서 각각 왼쪽과 오른쪽에서 삽입할 원소 x의 인덱스를 찾는 함수
# bisect_left(a, x)
# bisect_right(a, x)

# collections - 덱, 카운터
# 덱(deque) - 인덱싱, 슬라이싱 불가능 / 데이터의 시작과 끝 부분 데이터 추가 / 삭제가 용이

from collections import deque

data = deque([2, 3, 4])
data.appendleft(1)
data.append(5)

print("===========")
print(list(data))  # deque([1, 2, 3, 4, 5])

# 카운터(counter) - 개수
from collections import Counter

counter = Counter(['red', 'blue', 'red', 'green', 'blue'])
print("===========")
print(counter['blue'])  # 2
print(dict(counter))  # {'red': 2, 'blue': 2, 'green': 1}
print(counter)

# math - 팩토리얼, 제곱근, gcd, 삼각함수, 수학 상수
import math

print("===========")
print(math.factorial(5))  # 120
print(math.sqrt(4))  # 2.0
print(math.gcd(25, 15))  # 5

# f-string
answer = 7
print("===========")
print(f"정답은 {answer} 입니다.")

a = [1, 2, 3, 4, 5]
print("===========")
print(a)
print(*a)
print(*a, sep=" / ")
