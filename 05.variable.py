'''
작명 규칙
1. 알파벳, 숫자, 언더스코어(_)로 구성
2. 알파벳은 대/소문자 구분
3. 변수명의 시작은 숫자로 할 수 없음
4. 공백이나 특수 기호는 포함할 수 없음
5. Python 예약어는 사용할 수 없음

자료형 종류
Boolean = (True/False)
int = 0과 음수, 양수 값을 포함하는 숫자 값 (정수) = 42, -5
float = 소수점을 사용하는 숫자 값 (실수) = 3.14, -0.001
string = 따옴표로 묶여있는 문자열 값 = "hello", 'world'
list = 정수, 실수 및 문자열 등 자료들의 집합 (값의 집합) = []
tuple = 정수, 실수 및 문자열 등 자료들의 집합 (값의 집합) = ()
dict = 정수, 실수 및 문자열 등 자료들의 집합 (키와 값이 쌍으로 존재) = {key:value}
set = 정수, 실수 및 문자열 등 자료들의 집합 (중복, 순서 없음) = {}
NoneType = 값이 없음을 나타냄 = None

자료형 확인
type(변수명)

자료형 변환
int() = 정수형으로 변환
float() = 실수형으로 변환
str() = 문자열로 변환
bool() = 불리언으로 변환
list() = 리스트로 변환
tuple() = 튜플로 변환
set() = 집합으로 변환
dict() = 딕셔너리로 변환 (키-값 쌍 필요)
'''

x, y, z = 10, 10.0, '10'
print(type(x)) # <class 'int'>
print(type(y)) # <class 'float'>
print(type(z)) # <class 'str'>

'''
자료형 관련 에러
print(x + z) # int + str => Error!
Traceback (most recent call last):
  File "C:\python\05.variable.py", line 29, in <module>
    print(x + z)
          ~~^~~
TypeError: unsupported operand type(s) for +: 'int' and 'str'
'''

# 자료형 변환
# '10'을 숫자 10으로 변환
print(x + int(z)) # 20

a, b = 0, ''
print(bool(a)) # False (0은 False, 1 이상은 True)
print(bool(b)) # False (빈 값은 False, 값이 하나라도 있으면 True)