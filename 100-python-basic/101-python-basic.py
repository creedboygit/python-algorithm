# 사칙연산
# / : 나누기
# % : 나머지
# // : 몫
# ** : 제곱

# 리스트
# 초기화

a = [1, 2, 3, 4, 5]
print(a)

a = [0] * 5
print(a)

a = list()
print(a)

a = []
print(a)

a = [i for i in range(20)]
print(a)

a = [i for i in range(20) if i % 2 == 1]
print(a)

a = [i * i for i in range(1, 10)]
print(a)

# 2차원 리스트
# 2차원 리스트를 초기화할 땐 꼭 리스트 컴프리헨션을 사용해야 함
n = 3
m = 4
a = [[0] * m for _ in range(n)]
print(a)

# 리스트 메소드
# a = list()
a = [1, 2, 3, 4, 5]
a.sort()  # 오름차순 정렬
a.sort(reverse=True)  # 내림차순 정렬
a.reverse()  # 원소의 순서를 뒤집음
a.insert(2, 3)  # 인덱스 2에 원소 3을 삽입
a.remove(2)  # 값이 1인 원소를 제거. 원소가 여러 개면 한 개만 제거

# 인덱스로 제거
del a[1]
print("===========")
print(a)
a.pop(2)
print(a)

# insert 함수의 시간 복잡도는 O(N)_이므로, 남발하면 시간 초과날 수 있다.
# 특정 값의 원소를 모두 제거하려면 remove_set = {3, 5} 에 제거할 원소를 넣은 후
# result = [i for i in a if i not in remove_set] 으로 처리

a = [1, 2, 3, 3, 1, 2, 4, 5]
print("===========")
print(a)

# 삭제할 원소 집합 생성
remove_set = {1, 3}

# 리스트 컴프리센션 활용: 삭제할 원소 집합 데이터와 하나하나 비교
a_new = [i for i in a if i not in remove_set]
print("===========")
print(a_new)

# 문자열 연산
a = "Hello"
b = "World"

result = a + b
print(result)

result = a + "_" + b
print(result)

# 슬라이싱
result = a[2:]
print(result)

# 딕셔너리(사전)
price = dict()
price['사과'] = 9000
price['바나나'] = 7000
price['포도'] = 12000

print("===========")
print(price)

key_list = price.keys()
print(list(key_list))

value_list = price.values()
print(list(value_list))

if '사과' in price:  # 사전 자료형에 특정한 원소가 있는지 검사 가능
    print("'사과'가 존재합니다.")

if '풋사과' in price:  # 사전 자료형에 특정한 원소가 있는지 검사 가능
    print("'풋사과'가 존재합니다.")
else:
    print("'풋사과'가 존재하지 않습니다.")

# 집합
data = set([1, 1, 2, 3, 4, 4, 5])  # 중복이 제거됨 {1, 2, 3, 4, 5}
print("===========")
print(data)

data = {1, 1, 2, 2, 3, 3, 3, 4, 5, 5}  # 중복이 제거됨 {1, 2, 3, 4, 5}
print(data)

data.add("6")
print(data)

data.add(7)
print(data)

data.update([8, 9, "10"])  # 여러 개의 원소 추가
print(data)

data.remove("10")  # 특정한 값을 갖는 원소 삭제
print(data)

# a | b # 합집합
# a & b # 교집합
# a - b # 차집합

# global
aa = 3


def func():
    global aa
    aa += 1
    return aa


print(func())

# 람다
print((lambda a, b: a + b)(3, 7))  # 10

# 입출력
# input()은 한 줄의 문자열을 입력받을 수 있다.
# 여러 개의 정수 데이터를 입력받을 때는 list(map(int, input().split()))을 이용
# a = list(map(int, input().split()))
# print("===========")
# print(a)

# 만약 리스트가 아닌 각각의 변수에 저장하고 싶을 때
# n, m, k = map(int, input().split())
# n, m, k = input().split()
# print("===========")
# print(n)
# print(m)
# print(k)

# 시간 초과 문제로 입력을 최대한 빠르게 받아야 할 때 sys.stdin.readline() 을 이용
import sys

# a = sys.stdin.readline().rstrip()  # rstrip()은 맨 오른쪽의 줄바꿈 기호로 입력되는 엔터를 제거해주는 함수
# print(a)

# a, b, c = sys.stdin.readline().rstrip().split()  # rstrip()은 맨 오른쪽의 줄바꿈 기호로 입력되는 엔터를 제거해주는 함수
# print(a)
# print(b)
# print(c)

# f-string
answer = 7
print("===========")
print(f"정답은 {answer}입니다.")

a = [1, 2, 3, 4, 5]
print("===========")
print(*a)

# 파이썬 주요 라이브러리
# 내장 함수

result = min(76, 5, 4, 3)
print("===========")
print(result)

result = max(4, 5, 1, 3)
print(result)

result = sum([1, 2, 3, 4, 5])
print(result)

result = eval("(3 + 5) * 7")  # 수학 수식이 문자열 형식으로 들어오면 계산 결과를 반환
print(result)

# itertools - 파이썬에서 반복되는 형태의 데이터를 처리하는 기능 제공 - 순열, 조합 라이브러리 제공

from itertools import permutations  # 순열

data = ['A', 'B', 'C']
result = list(permutations(data, 3))
print("===========")
print(result)

from itertools import combinations  # 조합

result = list(combinations(data, 2))
print("===========")
print(result)

from itertools import product

result = list(product(data, repeat=3))  # 중복 허용 순열 (2개를 뽑는)
print("===========")
print(result)

from itertools import combinations_with_replacement

result = list(combinations_with_replacement(data, 2))  # 중복 허용 조합
print("===========")
print(result)

# 힙 기능을 제공하는 라이브러리로, 우선순위 큐 기능을 구현하기 위해 사용한다.
# 파이썬에서는 최소 힙을 제공하므로, 단순히 원소를 힙에 넣었다가 빼는 것만으로 오름차순 정렬이 완료된다.
# (최상단 원소는 항상 가장 작은 원소이므로)
import heapq


def heapsort(iterable):
    h = []
    results = []
    for value in iterable:
        heapq.heappush(h, value)  # 원소를 차례로 힙에 삽입
    for _ in range(len(h)):
        results.append(heapq.heappop(h))  # 원소를 차례로 꺼내어 result에 담음
    return results


data = ['3', '2', '5', '4', '3', '7']
print("===========")
print(heapsort(data))


### 최대힙 구현
# 최대 힙을 구현하는 방법은 원소의 부호를 바꾸어 힙에 삽입했다가, 원소를 꺼낸 뒤 다시 원소의 부호를 바꾸는 것이다.
def heapsort_max(iterable):
    h = []
    results = []
    for value in iterable:
        heapq.heappush(h, -value)
    for _ in range(len(h)):
        results.append(-heapq.heappop(h))
    return results


print("===========")
data = list(map(int, data))
print(f"data: {data}")
print(heapsort_max(data))

# bisect: 이진 탐색 기능을 제공하는 라이브러리
# 정렬된 배열에서 특정 원소를 찾아야할 경우 효과적
# bisect_left(a, x)  # 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 왼쪽 인덱스
# bisect_right(a, x)  # 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 오른쪽 인덱스

from bisect import bisect_left, bisect_right

a = [1, 2, 3, 3, 3, 4, 5]
bisect_left(a, 2)  # 1
bisect_right(a, 2)  # 2

# 이 두 함수는 정렬된 리스트에서 값이 특정 범위에 속하는 원소의 개수를 구하고자 할 때, 효과적으로 사용할 수 있다.
# 만약 2 이상 4 이하인 원소의 개수를 구하고 싶다면 다음과 같이 구할 수 있다.

a = [1, 2, 3, 3, 3, 4, 5]
result = bisect_right(a, 4) - bisect_left(a, 2)  # 6 - 1 = 5
print("===========")
print(f"2 이상 4 이하인 원소의 개수는 {result}개입니다.")

# collections: 덱, 카운터 등의 자료구조를 포함하는 라이브러리
from collections import deque

data = deque([2, 3, 4])
data.appendleft(1)
data.append(5)
print("===========")
print(data)
print(data.popleft())
print(data.pop())

# Counter는 등장 횟수를 세는 기능을 제공
# 원소별 등장 횟수를 세는 기능이 필요할 때 구현 가능
from collections import Counter

counter = Counter(['red', 'red', 'blue'])
print(counter)
print(counter['red'])

# math
import math

math.factorial(5)  # 5!
math.sqrt(7)  # 루트 7
math.gcd(21, 14)  # 최대 공약수

p = math.pi  # 파이 상수
e = math.e  # 자연 상수
print("===========")
print(e)
