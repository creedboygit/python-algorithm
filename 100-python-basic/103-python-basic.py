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
