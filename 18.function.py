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
