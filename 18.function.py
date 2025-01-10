"""
함수 기본 생성 방법
def 함수이름():
    수행 코드

------------------

pass
def func():
    pass

------------------

함수의 호출
def func():
    수행 코드
func()

------------------

func() # Error
def func():
    수행 코드

------------------

함수 사용 예시
def funcHello():
    print('Hello Python')
def funcVersion():
    print(''‘
    Title : Python Programming Basic
    Version : 1.0 Ver''')
funcHello()
funcVersion()

------------------

반환값이 있는 함수
def func():
    return 반환값

func()
"""

# 반환값 - 정수, 실수, 문자열


def funcInt():
    return 10


var = funcInt() + 10
print(var)  # 20


def funcFloat():
    return 0.1


var = funcFloat() + 10
print(var)  # 10.1


def funcStr():
    return "string"


var = funcStr() + "python"
print(var)  # 'stringpython'

# 반환값 - 튜플, 리스트, 딕셔너리


def funcTuple():
    return (1, 2, 3)


var = funcTuple()
print(var[0], var[1], var[2])  # 1 2 3


def funcList():
    return [1, 2, 3]


var = funcList()
print(var[0], var[1], var[2])  # 1 2 3


def funcDict():
    return {"a": 1, "b": 2}


var = funcDict()
print(var["a"], var["b"])  # 1 2

# argument(인자)


def func(arg):
    print(arg)


func(1)  # 1


def func(arg1, arg2):
    print(arg1, arg2)


func("a", "b")  # a b
# func("c")  # Error

# default argument (기본 인자)


def func(arg=1):
    print(arg)


func(5)  # 5
func()  # 1


def func(arg1, arg2=2):
    print(arg1, arg2)


func(5, 10)  # 5 10
func(5)  # 5 2

# keyword argument(키워드 인자)


def func(arg1, arg2):
    print(arg1, arg2)


func(5, 10)  # 5 10
func(arg2=3, arg1=1)  # 1 3


def func(arg1, arg2=1, arg3=2):
    print(arg1, arg2, arg3)


func(5, 2, 4)  # 5 2 4
func(5, arg3=4)  # 5 1 4

# variable argument(가변 인자)


def func(arg, *args):
    print(arg, args)


func(1, 2, 3, 4, 5)  # 1 (2, 3, 4, 5)

# keyword variable argument(키워드 가변 인자)


def func(arg, **kwargs):
    print(arg, kwargs)


func(1, key1=10, key2="a")  # 1 {'key1': 10, 'key2': 'a'}

# global 변수
a = 1
b = 2


def func():
    print(a, b)


func()  # 1 2
print(a, b)  # 1 2


# local 변수
def func():
    a = 1
    b = 2
    print(a, b)


func()  # 1 2
# print(a, b) # Error

# global, local
a, b = 1, 2


def func():
    a, b = 3, 4
    print(a, b)


func()  # 3 4
# print(a, b) # Error

# 예제 1
# programInfo() 함수를 만들어서 다음과 같은 정보가
# 표시 될 수 있도록 하시오
# Version : 1.0
# Update Date : 2017-01-01
# Author : Project Python


def programInfo():
    return "Version : 1.0\nUpdate Date : 2017-01-01\nAuthor : Project Python"


print(programInfo())

# 예제 2
# 사용자로 부터 값을 입력 받아서 사칙연산 프로그램을 함수로 구현하세요. (함수명은 calc()로 사용)


def calc():
    calc = input("계산할 수식을 입력하세요[ex) 5+5]: ")
    if "+" in calc:
        num1, num2 = calc.split("+")
        num1 = int(num1.strip())
        num2 = int(num2.strip())
        return num1 + num2
    if "-" in calc:
        num1, num2 = calc.split("-")
        num1 = int(num1.strip())
        num2 = int(num2.strip())
        return num1 - num2
    if "*" in calc:
        num1, num2 = calc.split("*")
        num1 = int(num1.strip())
        num2 = int(num2.strip())
        return num1 * num2
    if "/" in calc:
        num1, num2 = calc.split("/")
        num1 = int(num1.strip())
        num2 = int(num2.strip())
        return num1 / num2


print("===== 계산기 프로그램 =====")
while True:
    print("계산 결과 :", calc())
    en = input("계산을 종료하겠습니까?(yes/no):")
    if en == "yes":
        print(f"Thank you for using our program.")
        break
    else:
        continue


# 예제 3
# 사용자로 부터 값을 입력 받아서 사칙연산 프로그램을 함수로 구현하세요. (함수명은 calc()로 사용)
def calc(num1, num2, giho):  # calc()함수, 인자 3
    if giho == "+":
        sum = num1 + num2
        return sum  # Return을 이용한 함수 반환
    elif giho == "-":
        return num1 - num2
    elif giho == "*":
        return num1 * num2
    elif giho == "/":
        return num1 / num2


# main 프로그래밍
print("===== 계산기 프로그램 =====")
try:
    while True:  # 무한 반복구문
        in_text = input("계산할 수식을 입력하세요[ex) 5+5]: ")
        giho = ""
        num1 = num2 = 0
        if "+" in in_text:
            su1, su2 = in_text.split("+")
            num1 = int(su1.strip())
            num2 = int(su2.strip())
            giho = "+"
        elif "-" in in_text:
            su1, su2 = in_text.split("-")
            num1 = int(su1.strip())
            num2 = int(su2.strip())
            giho = "-"
        elif "*" in in_text:
            su1, su2 = in_text.split("*")
            num1 = int(su1.strip())
            num2 = int(su2.strip())
            giho = "*"
        elif "/" in in_text:
            su1, su2 = in_text.split("/")
            num1 = int(su1.strip())
            num2 = int(su2.strip())
            giho = "/"

        re = calc(num1, num2, giho)
        print("계산 결과 :", re)
        en = input("계산을 종료하겠습니까?(yes/no):")
        if en != "yes":
            continue
        else:
            break  # 위 선언된 함수를 호출
except:
    print("올바른 수식을 입력해 주세요. 나누기는 / 로 사용해 주세요.")


# 예제 4
# 짝, 홀수를 구분하는 함수를 작성해 주세요.
def evenodd(num):
    if num % 2 == 0:
        return "짝수"
    else:
        return "홀수"


try:
    while True:
        num = int(input("정수 입력: "))
        result = evenodd(num)
        print(result)
        en = input("계산을 종료하겠습니까?(yes/no):")
        if en != "yes":
            continue
        else:
            break
except:
    print("정수를 입력해 주세요.")


# 예제 5
# "3"의 배수를 판별하는 함수를 작성해 주세요.
def multiple(num):
    if not num % 3:
        print("3의 배수 입니다.")
    else:
        print("3의 배수가 아닙니다.")


try:
    while True:
        num = int(input("정수 입력: "))
        result = multiple(num)

        en = input("계산을 종료하겠습니까?(yes/no):")
        if en != "yes":
            continue
        else:
            break  # 위 선언된 함수를 호출
except:
    print("정수를 입력해 주세요.")


# 예제 6
# 거꾸로 수를 반환하는 함수를 계산,출력 기능으로 나눠서 작성해 주세요
# 예) 123 => 321
def reverseCode(result):
    temp, su = 0, 0
    while True:
        temp = result % 10
        result = result // 10
        su = (su + temp) * 10
        if not result:
            return su // 10


def display():
    result, su = 0, 0
    result = int(input("정수 입력: "))
    su = reverseCode(result)
    print("변환 전 값: {}, 변환 후 값: {}".format(result, su))


display()

# 예제 7
# 예제 친구이름 관리를 함수로 기능을 나눠서 작성해주세요.
# (1.친구목록보기,
#  2.친구추가,
#  3.친구삭제,
#  4.친구수정,
#  0.종료)
import os


def fr_list(lst):
    print(lst)
    print("======== 친구 리스트 ========")
    if lst != []:
        print(lst)
        for i in range(len(lst)):
            print("{} : {}".format((i + 1), lst[i]))
    else:
        print("등록된 친구가 없습니다.")


def fr_add(lst):
    name = input("추가할 친구 이름을 입력하세요: ")
    lst.append(name)


def fr_del(lst):
    name = input("삭제할 친구 이름을 입력하세요: ")
    lst.remove(name)


def fr_mod(lst):
    name = input("친구 이름을 입력하세요: ")
    idx = lst.index(name)
    print(lst)
    print(idx)
    lst[idx] = input("변경할 이름을 입력하세요: ")


lst = []
while True:
    os.system("cls")
    print("================ 친구 관리 프로그램 ==================")
    print(" 1. 친구목록 보기")
    print(" 2. 친구추가")
    print(" 3. 친구삭제")
    print(" 4. 친구수정")
    print(" 0. 종료")
    sel = int(input("메뉴를 선택해주세요[0 ~ 4]: "))
    if sel == 1:
        fr_list(lst)
        os.system("pause")
    elif sel == 2:
        fr_add(lst)
        os.system("pause")
    elif sel == 3:
        fr_del(lst)
        os.system("pause")
    elif sel == 4:
        fr_mod(lst)
    elif sel == 0:
        print("프로그램 종료합니다..")
        os.system("pause")
        break
    else:
        print("메뉴 선택을 잘못했습니다.")


# 예제 8
# 비만도를 구하는 함수를 만드시오.
#    비만도 계산 식 : 비만도(%) = 현재 체중 / 표준 체중 * 100
#    표준 체중 계산 식 : 표준 체중 = (현재 키 – 100) * 0.9
#    출력 예제 : 홍길동님의 비만도는 112.15% 입니다.


def fatRate(tall, weight):
    std_weight = (tall - 100) * 0.9
    fat_rate = weight / std_weight * 100

    return fat_rate


print("{}님의 비만도는 {:.2f}% 입니다.".format("홍길동", fatRate(175.3, 72.1)))
print("{}님의 비만도는 {:.2f}% 입니다.".format("박찬호", fatRate(183.7, 86.9)))


# 예제 9
# 알바 시급 프로그램으로 다음 값들이 고정되어 있습니다.
# 시급 : 8500원, 하루 8시간, 한달에 30일(기본)

#  (다음과 같이 나오게 만들기)
#  시급 계산 프로그램
#  1.기본급
#  2.일한 날짜 입력
#  번호 선택 >>


def alba(day=30):
    time = 8
    pri = 8500  # time=8(local), pri=8500(시급)
    result = day * time * pri  # day default(30)
    return result


def display():
    num = int(
        input(
            "시급 계산 프로그램\n1.기본급\n2.일한 날짜 입력\n\
번호 선택 >>"
        )
    )
    if num == 1:  # 기본급 결과를 출력(30기준으로 출력)
        re = alba()
    elif num == 2:  # 30일 미만인 경우 계산 날짜 입력 받음
        day = int(input("일한 일수 입력>> "))
        re = alba(day)
    print("당신의 급여는 {:,}원 입니다.".format(re))


# time 전역변수(global)
# main 코드 시작지점
display()


# 예제 10
# 디폴트 매개변수를 이용한 요금 구하는 프로그램 만들기.
# 기본요금 500원 환승이 없거나 환승 1회까지는 기본 요금.
# 1회를 초과하는 환승의 경우 환승 1회마다 요금의 2배씩 증가된다.
# ( EX: 환승 2회일 경우 : 1000원 , 환승 3회일 경우 : 2000원 )
# ( 장거리는 10000원으로 처리한다. )
# 1. 환승 안함
# 2. 환승 함
# 3. 장거리


def transfer(dest, su=1, won=500):
    for i in range(1, su):
        won *= 2
        if won >= 10000:
            won = 10000
    return "{}까지 요금: {:,}원 입니다.".format(dest, won)


def display():
    dest = ""
    su = 0
    num = int(input("1.환승 안 함\n2.환승 함\n3.장거리\n번호 선택 >> "))
    dest = input("목적지의 입력: ")
    if num == 1:
        result = transfer(dest)
    elif num == 2:
        su = int(input("환승 횟 수 입력: "))
        result = transfer(dest, su)
    elif num == 3:
        result = transfer(dest, 1, 10000)
    else:
        print("번호를 다시 선택하세요.")
        return
    print(result)


display()  # main Code


# 예제 11
# 평균을 구하는 함수
def avg(*args):
    avg = 0
    for x in args:
        avg += x
    return avg / len(args)


print(avg(4, 6, 8, 3, 9))
