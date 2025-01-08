"""
기본 사용법
변수명 = (value1, value2, ...)
변수명 = tuple([value1, value2, ...])
"""

tup = (1, 2, 3)

# 인덱싱
print(tup)
print(tup[0])
print(tup[1])

print(tup)
print(tup[-1])
print(tup[-3])

# 슬라이싱
print(tup)
print(tup[0:2])
print(tup[1:3])

print(tup)
print(tup[-3:-1])
print(tup[-2:])

# 튜플 - 반복문
tup = ("a", "b", "c", "d")
for idx in range(4):
    print(tup[idx])

for idx in range(len(tup)):
    print(tup[idx])

for val in tup:
    print(val)

# Packing, Unpacking
p = (1, 2), (3, 4)
x, y = p

# 2차 튜플
tup = (("a", "b"), ("c", "d"), ("e", "f"))
print(tup[0])  # ('a', 'b')
print(tup[1])  # ('c', 'd')
print(tup[2][0])  # 'e'

for val in tup:
    print(val[0], val[1])

for val1, val2 in tup:
    print(val1, val2)

tup = (1, 2, 3, 1, 2)

# count
tup.count(2)

# index
tup.index(2)

menu = (
    ("칼국수", 6000),
    ("비빔밥", 5500),
    ("돼지국밥", 7000),
    ("돈까스", 7000),
    ("김밥", 2000),
    ("라면", 2500),
)

# 예제 1
# 김밥과, 라면의 가격을 각각 출력 하시오
print(menu[4][1], menu[5][1])

# 예제 2
# 가격이 7000에 해당하는 메뉴를 출력 하시오
for m, p in menu:
    if p == 7000:
        print(m)

# 예제 3
# 가격이 6000원 이하인 메뉴를 출력 하시오
for m, p in menu:
    if p <= 6000:
        print(m)

# 예제 4
# 사용자 입력으로 메뉴를 입력 받아 해당하는 메뉴의 가격을
# 출력하시오
input_menu = input("메뉴를 입력하세요: ")
for m, p in menu:
    if input_menu == m:
        print(p)

# 예제 5
# 사용자 입력으로 1개 이상의 메뉴를 입력 받아
# 해당 메뉴의 총 가격을 출력하시오
while True:
    price = 0
    menu_list = tuple(input("메뉴를 입력하세요: ").split(","))
    for l in menu_list:
        for m, p in menu:
            if l == m:
                price += p
    print(price)
    if input_menu == "exit":
        break
