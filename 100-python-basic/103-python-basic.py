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

