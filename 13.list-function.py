"""
append(value) 리스트 끝에 값을 추가함
extend(iter) 리스트 끝에 list, tuple, dict의 값을 하나씩 추가함
insert(idx, value) 특정 인덱스 위치에 값을 추가함
pop([idx]) 마지막 인덱스의 값을 반환 후 삭제함 인덱스 번호를 저장할 수도 있음
remove(value) 특정 값에 해당하는 것을 찾아 삭제함
clear() 모든 값을 삭제하여 빈 리스트만 남김
count(value) 리스트에서 일치하는 값의 수를 반환함
index(value) 리스트에서 일치하는 값의 인덱스 번호를 반환함
reverse() 리스트의 모든 값을 뒤집어 나열함
sort([reverse=False]) 리스트의 값을 오름차순(False) 내림차순(True) 정렬함
"""

# append
lst = [1, 2, 3]
lst.append("a")
lst.append([4, "b"])

# extend
lst = [1, 2, 3]
lst.extend(["a", "b", "c"])

# insert
lst = [1, 2, 3]
lst.insert(1, "b")

# pop
lst = [1, 2, 3]
lst.pop()
lst.pop(0)

# remove
lst = [1, 2, 3]
lst.remove(2)

# clear
lst = [1, 2, 3]
lst.clear()

# count
lst = [1, 2, 3, 1]
lst.count(1)

# index
lst = [1, 2, 3, 1]
lst.index(1)
lst.index(1, 1)

# reverse
lst = [1, 3, 2]
lst.reverse()

# sort
lst = [1, 3, 2]
lst.sort()
lst.sort(reverse=True)

menu = [
    ["칼국수", 6000],
    ["비빔밥", 5500],
    ["돼지국밥", 7000],
    ["돈까스", 7000],
    ["김밥", 2000],
    ["라면", 2500],
]

# 예제 1
# 비빔밥과, 돈까스의 가격을 출력 하시오
print(menu[1], menu[3])

# 예제 2
# 사용자 입력으로 메뉴와 가격을 입력 받아
# menu 변수에 자료를 추가하는 코드를 작성 하시오
input_menu = input("메뉴를 입력하세요: ")
input_price = int(input("가격을 입력하세요: "))
menu.append([input_menu, input_price])

# 예제 3
# 사용자 입력으로 메뉴와 가격을 입력 받아
# menu 변수에 자료를 추가 할 때 기존에 동일한 메뉴가
# 존재하는 경우 가격만 변경 되도록 코드를 작성 하시오
input_menu = input("메뉴를 입력하세요: ")
input_price = int(input("가격을 입력하세요: "))
for m in menu:
    if m[0] == input_menu:
        m[1] = input_price
print(menu)

# 예제 4
# 메뉴를 자동으로 선택하여 출력하는 코드를 작성 하시오
from random import randint

print(menu[randint(0, len(menu) - 1)])
