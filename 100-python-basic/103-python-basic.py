# 실수형
# 소수부가 0일 때 0을 생략
a = 5.  # 5.0
print(a)

# 10억의 지수 표현 방식 (최단 경로문제에서 자주 사용)
a = 1e9  # 100000000.0
print(a)

# 컴퓨터는 2진수 체계이기 때문에 실수 덧셈을 정확히 못함. 보통 5번째 자리에서 반올림하면 됨
a = 0.3 + 0.6
print(a)
print(round(a, 4))

# 수 자료형의 연산
a = 7
b = 3

print(a / b)
print(a % b)  # 나머지
print(a // b)  # 몫
print(a ** b)

# 리스트 초기화
a = [1, 2, 3, 4, 5]

print(a)
print(a[3])

# 빈 리스트 선언
a = list()
a = []

# 크기가 n이고 모든 값이 0인 1차원 리스트 초가화
n = 10
a = [0] * n
print(a)

# 리스트 슬라이스
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(a[-1])
print(a[-3])
print(a[1:4])

# 리스트 컴프리헨션
# 리스트를 초기화하는 방법 중 하나
# 대괄호 안에 조건문과 반복문을 넣는 방식으로 리스트를 초기화할 수 있다.
# 2차원 리스트를 초기화할 때 매두 효과적으로 사용된다.
# 리스트 컴프리헨션과 일반 소스 코드 비교

# 0부터 19까지의 숫자 중에서 홀수만 포함하는 리스트

array = [i for i in range(20) if i % 2 == 1]
print(array)

array2 = []
for i in range(20):
    if i % 2 == 1:
        array2.append(i)
print(array2)

# 1부터 9까지의 수의 제곱 값을 포함하는 리스트
array3 = [i * i for i in range(1, 10)]
print(array3)

# N * M 크기의 2차원 리스트 초기화
n = 3
m = 4

array4 = [[0] * m for _ in range(n)]
print(array4)

# 특정 크기의 2차원 리스트를 초기화할 때는 반드시 리스트 컴프리헨션을 사용

# N * M 크기의 2차원 리스트 초기화 (잘못된 방법)
n = 3
m = 4
array = [[0] * m] * n
print(array)

array[1][1] = 5
print(array)
# 내부적으로 3개의 리스트가 모두 동일한 객체에 대한 3개의 레퍼런스로 인식되기 때문

# 리스트 관련 메서드
a = [1, 4, 5, 3, 2]

# 리스트에 원소 삽입
a.append(2)
print(a)

# 오름차순 정렬
a.sort()
print(a)

# 내림차순 정렬
a.sort(reverse=True)
print(a)

# 리스트 원소 뒤집기
a.reverse()
print(a)

# 특정 인덱스에 데이터 추가
a.insert(2, 3)
print(a)

# 특정 값인 데이터 개수 세기
print(a.count(3))

# 특정 값 데이터 삭제 (인덱스가 낮은 것 하나)
a.remove(1)
print(a)

# 특정한 값을 갖는 원소를 삭제하려면?
# 시간 복잡도를 고려해서 remove 는 사용하지 않는 것을 추천

a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}

# remove_set에 포함되지 않는 값만을 저장
result = [i for i in a if i not in remove_set]
print(result)

# 문자열 연산
a = "hello"
b = "creed"

print(a * 3)

a = "ABSDF"
print(a[2:4])

# 튜플
# 튜플은 한버 선언된 값을 변경할 수 없다.
# 리스트는 대괄호[]를 이용하지만, 튜플은 소괄호 ()를 이용한다.
# 그래프 알고리즘을 구현할 때 자주 사용
# 다익스트라 최단 경로 알고리즘 (우선순위큐 사용)
# (비용, 노드번호) 형태로 튜플을 묶어서 관리

a = (1, 2, 3, 4)
# a[2] = 7

# 사전(딕셔너리) 자료형
# key와 value의 쌍을 데이터로 가지는 자료형
# 딕셔너리에 특정한 원소가 있는지 검사할 때는 '원소 in 사전' 형태를 사용할 수 있다.

data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['수박'] = 'Watermelon'

print(data)

if '사과' in data:
    print("'사과'를 키로 가지는 데이터가 존재합니다.")

if '포도' in data:
    print("'포도'를 키로 가지는 데이터가 존재합니다.")
else:
    print("'포도'를 키로 가지는 데이터가 존재하지 않습니다.")

# 딕셔너리 관련 함수
# key 데이터만 뽑아서 리스트로 이용할 때는 keys() 함수
# value 데이터만 뽑아서 리스트로 이용할 때는 values() 함수

# 키 데이터만 담은 리스트
key_list = data.keys()
print("===========")
print(key_list)

value_list = data.values()
print(value_list)

for key in key_list:
    print(data[key])

# 집합 자료형 (Set)
# 중복을 허용하지 않는다
# 순서가 없다
# 특정한 데이터가 이미 등장한 적이 있는지 여부를 체크할 때 효과적이다.

data = set([1, 1, 2, 3, 4, 3, 4, 5])
print("===========")
print(data)

data = {1, 2, 2, 3, 3, 4, 5}
print(data)

# 집합 자료형의 연산
# 합집합, 교집합, 차집합 연산이 있다.
a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}

print(a | b)
print(a & b)
print(a - b)
print(b - a)

# 집합 자료형 관련 함수
data = {1, 2, 3}
print(data)

# 새로운 원소 추가
data.add(4)
print(data)

# 새로운 원소 여러 개 추가
data.update([4, 5, 6])
print(data)

# 특정한 값을 갖는 원소 삭제
data.remove(3)
print(data)

# 파이썬에서는 추가적으로 in 연산자와 not in 연산자를 제공한다.
# 자료형 (리스트, 튜플, 문자열, 딕셔너리) 에 사용된다.
# pass문 (조건문의 값이 참이라고 해도 아무것도 처리하고 싶지 않을 때)

# x in 리스트 - 리스트 안에 x가 들어가 있을 때 True
# x not in 문자열 - 문자열 안에 x가 들어가 있지 않을 때 True

score = 70
if score >= 80:
    pass
else:
    print('성적이 80점 미만입니다.')

# 1줄일 경우 줄이기
if score >= 80:
    result = "Success"
else:
    result = "Fail"

# 3항 연산자
result = score >= 80 and "Success" or "Fail"
print("===========")
print(result)

# 리스트에 있는 원소의 값을 변경해서 또 다른 리스트를 만들고자 할 때 매우 간결하게 사용 가능
a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}

result = []
for i in a:
    if i not in remove_set:
        result.append(i)

print(result)

result2 = [i for i in a if i not in remove_set]
print(result2)

# while문
i = 1
result = 0

while i <= 9:
    result += i
    i += 1
print(result)

# for문
# range (시작값, 끝값 + 1, 증감)
# continue
# break

result = 0

for i in range(1, 10):
    result += 1
    # print(result)
print(result)

scores = [90, 85, 77, 65, 98]
cheating_list = {2, 4}

for i in range(5):
    if i + 1 in cheating_list:
        continue
    if scores[i] >= 80:
        print(i + 1, '번 학생은 합격입니다.')

# 이중 for문
# 플로이드 워셜 알고리즘
# 다이나믹 프로그래밍

# 구구단
print("===========")
for i in range(2, 10):
    for j in range(1, 10):
        print(i, "X", j, "=", i * j)
    print()


# 함수
# 동일한 알고리즘을 반복적으로 수행해야 할 때 사용
# 매개변수나 return은 존재하지 않을 수도 있다.


def add(a, b):
    return a + b


print(add(3, 7))


def add(a, b):
    print("함수의 결과:", a + b)


add(b=3, a=9)

# global
# 함수 안에서 함수 밖의 변수 데이터를 변경해야 하는 경우

a = 0


def func():
    global a
    a += 1


for i in range(10):
    func()

print(a)


# 람다 표현식 (Lambda Express)
# 특정한 기능을 수행하는 함수를 한 줄에 작성할 수 있다.
# 람다식은 파이썬의 정렬 라이브러리를 사용할 때, 정렬 기준(Key)를 설정할 때에도 자주 사용된다.

def add(a, b):
    return a + b


print(add(3, 7))

# 람다 표현식으로 구현한 add() 메서드
print((lambda a, b: a + b)(3, 7))

# 입출력
# 입력
# map() : 해당 리스트의 모든 원소에 int() 함수를 적용한다.
# sys.stdin.readline()
# 입력을 최대한 빠르게 받아야 하는 경우
# readline()으로 입력하면 입력 후 엔터가 줄 바꿈 기호로 인식, 공백 문자를 제거하려면 rstrip() 함수를 사용해야 함

# 데이터의 개수 입력
# n = int(input())

# 각 데이터를 공백으로 구분하여 입력
# data = list(map(int, input().split()))

# data.sort(reverse=True)
# print(data)

# 공백을 기준으로 구분하여 적은 수의 데이터 입력
# n, m, k = map(int, input().split())

# 입력을 최대한 빠르게 받아야 하는 경우
import sys

# 문자열 입력받기
# data = sys.stdin.readline().rstrip()
# print(data)

# 출력
# print()
# 기본적으로 출력 이후에 줄바꿈을 수행
# f-string

# 출력할 변수들
a = 1
b = 2

print(a, b)

# 출력 시 오류가 발생하는 소스코드 예시 (자바와 다름 주의)

# 출력할 변수들
answer = 7

# print("정답은 " + answer + "입니다.") # 오류 남

# 올바른 예
print("정답은 " + str(answer) + "입니다.")
print("정답은", str(answer), "입니다.")

answer = 8
print(f"정답은 {answer}입니다.")

# 1. 내장 함수
# print(), input() 과 같은 기본 입출력 기능부터 sorted()와 같은 정렬 기능을 포함하고 있는 내장 라이브러리

# 2. itertools
# 파이썬에서 반복되는 형태의 데이터를 처리하는 기능을 제공하는 라이브러리, 순열과 조합 라이브러리를 제공

# 3. heapq
# 힙(Heap) 기능을 제공하는 라이브러리. 우선순위 큐 기능을 구현하기 위해 사용

# 4. bisect
# 이진탐색/이분탐색(binary search) 기능을 제공하는 라이브러리

# 5. Collections
# 덱(deque), 카운터(Counter) 등의 유용한 자료구조를 포함하고 있는 라이브러리

# 6. math
# 필수적인 수학적 기능을 제공하는 라이브러리
# 팩토리얼, 제곱급, 최대공약수(GCD), 삼각함수, 파이(pi)

result = [1, 2, 3, 4, 5]

print("===========")
print(sum(result))  # iterable 객체가 들어왔을 때 (반복 가능한 객체) - 리스트, 딕셔너리, 튜플 자료형

print(min(result))
print(max(result))

result = eval("(3 + 5) * 7")

print(result)

result = sorted([9, 3, 2, 4, 5, 1])  # 오름차순 정렬
print(result)

result = sorted([9, 3, 2, 4, 5, 1], reverse=True)  # 기존 객체는 변경되지 않으며 return 값이 존재한다.
print(result)

result.sort()  # void문이다. result가 변경된다.

print(result)

data = [('김진선', 33), ('이진희', 23), ('마이클', 45)]
result = sorted(data, key=lambda x: x[1], reverse=True)
print(result)

data = ["23", "59", "59"]
print(":".join(data))

# itertools
# 반복되는 데이터를 처리하는 기능을 포함하고 있는 라이브러리
# permutations(순열)
# combinations (조합)
# product (중복을 허용하는 순열)
# combinations_with_replacement (중복을 허용하는 모든 조합)
# 순열 조합 모두 클래스이므로 객체 초기화 이후 리스트 자료형으로 변환하여 사용한다.

from itertools import permutations, combinations, product, combinations_with_replacement

data = ['a', 'b', 'c']  # 데이터 준비

# 리스트에서 3개를 뽑아 나열하는 모든 경우를 출력
result = list(permutations(data, 3))  # 모든 순열 구하기
print(result)

result = list(combinations(data, 2))  # 2개를 뽑는 모든 조합 구하기
print(result)

result = list(product(data, repeat=2))  # 2개를 뽑는 모든 순열 구하기 (중복 허용)
print(result)

result = list(combinations_with_replacement(data, 2))  # 2개를 뽑는 모든 조합 구하기 (중복 허용)
print(result)

# heapq (Min heap)
# 힙 기능을 위해 heapq 라이브러리를 제공
# 다익스트라 최단 경로 알고리즘 등에서 우선순위 큐 기능을 구현하고자 할 때 사용
# PriorityQueue 라이브러리를 사용할 수 있지만 코딩 테스트 환경에서는 heapq가 더 빠르게 동작하므로 heapq를 사용
# 최소 힙(min heap)으로 구성되어 있으므로 넣었다 빼는 것만으로 O(N log N) 에 오름차순 정렬이 완료된다.
# heapq.heappush() 삽입
# heapq.heappop() 꺼냄

# 힙정렬(heap sort)을 heapq로 구현하는 예제

import heapq


def heapsort(iterable):
    h = []
    result = []

    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)

    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))

    return result


result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print("===========")
print(result)

# 부호를 사용하여 최대 힙(max heap)구현
import heapq


def heapsort(iterable):
    h = []
    result = []

    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, -value)

    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(-heapq.heappop(h))

    return result


result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print("===========")
print(result)

# bisect
# 이진 탐색을 쉽게 구현할 수 있도록 하는 라이브러리
# 정렬된 배열에서 특정한 원소를 찾아야할 때 매우 효과적으로 사용
# bisect_left(a, x) - 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 왼쪽 인덱스를 찾는 메서드
# bisect_right(a, x) - 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 오른쪽 인덱스를 찾는 메서드
# 정렬된 리스트에서 값이 특정 범위에 속하는 원소의 개수를 구하고자 할 때 사용
from icecream import ic

from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
x = 4

ic(bisect_left(a, x))
ic(bisect_right(a, x))


# 정렬된 리스트에서 값이 특정 범위에 속하는 원소의 개수를 구하고자 할 때 사용
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index


# 리스트 선언
a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

# 값이 4인 데이터 개수 출력
ic(count_by_range(a, 4, 4))

# 값이 [01, 3] 범위에 있는 데이터 개수 출력
ic(count_by_range(a, -1, 3))

# collections
# 유용한 자료구조를 제공하는 표준 라이브러리

# deque
# 스텍, 큐를 구현할 때 사용하는 라이브러리
# 가장 앞 원소 추가, 가장 앞 원소 제거에서 O(1)의 시간 복잡도를 가진다.
# 인덱싱, 슬라이싱 등은 사용할 수 없다

from collections import deque

data = deque([2, 3, 4])
data.appendleft(1)
ic(data)
data.append(5)
ic(data)

data.pop()
ic(data)
data.popleft()
ic(data)

ic(list(data))

# Counter
# 등장 횟수를 세는 기능을 제공
# 리스트와 같은 iterable 객체가 주어졌을 때, 해당 객체 내부의 원소가 몇 번씩 등장했는지를 알려준다.
# 원소별 등장 횟수를 세는 기능이 필요할 때 짧은 코드로 이를 구현할 수 있다.
from collections import Counter

counter = Counter(['red', 'blue', 'green', 'blue', 'blue'])
ic(counter)
ic(counter['blue'])
ic(dict(counter))

# math
import math

ic(math.factorial(5))  # 5 팩토리얼
ic(math.sqrt(7))  # 제곱근
ic(math.gcd(21, 14))  # 최대공약수
ic(math.pi)  # 파이
ic(math.e)  # 자연상수
