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
