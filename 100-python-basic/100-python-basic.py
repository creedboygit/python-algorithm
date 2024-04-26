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
print("===========")


