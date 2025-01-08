"""
기본 사용법
변수명 = {}
변수명 = {key1:value1, key2:value2, ...}
변수명 = dict([(k1, v1), (k2, v2), ...])
"""

# 키를 가지고 값에 접근
# print(dic[key])
# dic[key] = value # 값 변경

dic = {"a": 1, "b": 2, "c": 3}
print(dic["a"])
dic["c"] = 5 * dic["b"]
print(dic["c"])

# 반복문
dic = {"a": 1, "b": 2, "c": 3}
for k in dic:
    print(k, dic[k])

# 리스트
dl = {
    "음료": ["탄산", "과일", "우유", "물"],
    "식사": ["김밥", "라면", "돈까스", "비빔밥"],
}
for key in dl:
    print(dl[key])

ld = [
    {"name": "Park", "age": 25, "blood": "B"},
    {"name": "Kim", "age": 27, "blood": "A"},
]

for dic in ld:
    print(dic["name"], dic["age"], dic["blood"])

# 딕셔너리
dd = {"Park": {"age": 25, "blood": "B"}, "Kim": {"age": 37, "blood": "A"}}

for name in dd:
    print(name, dd[name]["age"], dd[name]["blood"])

"""
딕셔너리 함수
update(dict) 사전형 자료에 값을 추가함
fromkeys(iter[, value]) 리스트, 튜플에 존재하는 값을 키로 사전형 자료를 생성하여 반환함
get(key[, value]) 사전형의 키를 통해 값을 반환함
keys() 사전형의 모든 키를 반환함
values() 사전형의 모든 값을 반환함
items() 사전형의 모든 키-값의 쌍을 튜플로 반환함
pop(key) 사전형의 키를 통해 값을 반환 후 삭제함
popitem() 사전형의 키-값의 쌍을 튜플로 반환 후 삭제함
clear() 사전형의 모든 키-값을 삭제하여 빈 사전형 자료만 남김
"""

# update
dic = {"a": 1, "b": 2, "c": 3}
dic.update({"a": 4, "d": 5})
print(dic)

# fromkeys
k = ["a", "b", "c", "d"]
dic1, dic2 = {}, {}
dic1 = dic1.fromkeys(k)
dic2 = dic2.fromkeys(k, 1)
print(dic1)
print(dic2)

# get
# key가 없어도 예외가 발생하지 않음.
dic = {"a": 1, "b": 2, "c": 3}
print(dic.get("b"))
print(dic.get("d", "Not exist key"))
print(dic)

# keys
dic = {"a": 1, "b": 2, "c": 3}
for key in dic.keys():
    print(key)

# values
dic = {"a": 1, "b": 2, "c": 3}
for value in dic.values():
    print(value)

# items
dic = {"a": 1, "b": 2, "c": 3}
for key, value in dic.items():
    print(key, value)

# pop
dic = {"a": 1, "b": 2, "c": 3}
dic.pop("b")
print(dic)

# popitem
dic = {"a": 1, "b": 2, "c": 3}
dic.popitem()
print(dic)

# clear
dic = {"a": 1, "b": 2, "c": 3}
dic.clear()
print(dic)

# 예제 1
# 다음의 메뉴와 가격을 Key와 Value로 사용하여
# 사전형 자료를 만드시오 (변수명은 menu)
# 칼국수(6000원), 비빔밥(5500원), 돼지국밥(7000원),
# 돈까스(7000원), 김밥(2000원), 라면(2500원)
menu = {
    "칼국수": 6000,
    "비빔밥": 5500,
    "돼지국밥": 7000,
    "돈까스": 7000,
    "김밥": 2000,
    "라면": 2500,
}

# 예제 2
# 위에서 만든 사전형 자료 menu 변수에서
# 가격이 6000원 미만에 해당하는 메뉴와 가격을 출력하는
# 코드를 작성하시오
for m, p in menu.items():
    if p < 6000:
        print(m)

# 예제 3
# 사용자 입력으로 메뉴와 가격을 입력 받아
# menu 변수에 자료를 추가 할 수 있도록 하시오
# (동일한 메뉴는 가격만 변경)
input_menu = input("메뉴를 입력하세요: ")
input_price = int(input("가격을 입력하세요: "))
for m, p in menu.items():
    if m == input_menu:
        p = input_price
    else:
        break
menu.update({input_menu: input_price})
print(menu)

# 예제 4
# 메뉴를 자동으로 선택하여 출력하는 코드를 작성 하시오
