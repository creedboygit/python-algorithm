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
