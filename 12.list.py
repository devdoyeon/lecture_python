"""
기본 사용법
변수명 = []
변수명 = [value1, value2, ...]
변수명 = list((value1, value2, ...))
"""

# 인덱싱
lst = [1, 2, 3]
print(lst)
print(lst[0])
print(lst[1])

lst = [1, 2, 3]
lst[0] = "a"
lst[2] = lst[1] * 2
lst[1] = lst[0] * lst[2]

lst = [1, 2, 3]
print(lst)
print(lst[-1])
print(lst[-3])

lst = [1, 2, 3]
lst[-3] = "b"
lst[-1] = lst[1] * 2
lst[-2] = lst[0] * lst[2]

# 슬라이싱
lst = [1, 2, 3]
print(lst)
print(lst[-3:-1])
print(lst[-2:])

lst = [1, 2, 3]
lst[-3:-1] = [4, 8]
lst[-2:] = "c", "d"

# 반복문
lst = [1, 2, 3]
for value in lst:
    print(value)

lst = [1, 2, 3]
for idx in range(3):
    lst[idx] = lst[idx] + 1
    print(lst[idx])

lst = [1, 2, 3]
for idx in range(len(lst)):
    lst[idx] = lst[idx] + 1
    print(lst[idx])

# 2차 리스트
lst = [["a", "b"], ["c", "d"], ["e", "f"]]
print(lst[0])  # ['a', 'b']
print(lst[1])  # ['c', 'd']
print(lst[2][0])  # 'e'

lst = [["a", "b"], ["c", "d"], ["e", "f"]]
for val in lst:
    print(val[0], val[1])

lst = [["a", "b"], ["c", "d"], ["e", "f"]]
for val in lst:
    for x in val:
        print(x, end=" ")
    print()

lst = [["a", "b"], ["c", "d"], ["e", "f"]]
for idx in range(len(lst)):
    for idy in range(len(lst[idx])):
        lst[idx][idy] = idx + idy
        print(lst[idx][idy], end=" ")

# Iterable
list_1 = [1, 2, 3, 4, 5]
print(list_1)
list_2 = iter(list_1)
print(next(list_2))
print(next(list_2))
print(next(list_2))
print(next(list_2))

# for
list_1 = [1, 2, 3, 4, 5]
for x in list_1:
    print(x)
