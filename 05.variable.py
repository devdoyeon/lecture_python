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
  File "05.variable.py", line 29, in <module>
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

# 예제 1
# 다음의 변수에 저장되어 있는 값을 활용하여
# 동일한 결과가 나오도록 하시오
# x, y, z = '100', 10.5, 20
# 1. 110.5
# 2. 10020
# 3. 10.520.0
# 4. 110.520
x, y, z = '100', 10.5, 20

print(int(x) + y) # 110.5
print(x + str(z)) # 10020
print(str(y)+str(z)+'.0') # 10.520.0
print(str(int(x)+y)+str(z)) # 110.520

# 예제 2
# Linux 의 수업료가 500,000원이고 Windows 수업료는  400,000원이다.
# 9월 수강생이 Linux를 30명 수강하고 Windows는 20명 수강한다.
# 월 수업료 총액을 계산하는 프로그램을 작성하세요.
linux = 500000
windows = 400000
print(f'총액은 {format(linux * 30 + windows * 20, ',')}원입니다.')

# 예제 3
# 1번 문제에서 구한 수업료 총액에서  Linux과 Windows의 수업료가
# 각각 5%, 10% Discount한 경우에 손실액을 구하는 프로그램을 작성하세요.
print(f'Linux 수업의 손실액은 {format(int(linux * 0.05), ',')}원, Windows 수업의 손실액은 {format(int(windows * 0.1), ',')}원 입니다.')

# 예제 4
# 우리나라는 섭씨 온도를 사용하는 반면 미국과 유럽은 화씨 온도를 주로 사용합니다.
# 화씨 온도(F)를 섭씨 온도(C)로 변환할 때는 다음과 같은 공식을 사용합니다.
# 이 공식을 사용해 화씨 온도가 50일 때의 섭씨 온도를 계산해 보세요.
# C = (F-32)/1.8
F = 50
print(f'화씨 온도가 {F}도일 때 섭씨 온도는 {int((F-32)/1.8)}도입니다.')

# 예제 5
# 화면에 "Linux"를 10번 출력하는 프로그램을 작성하세요.
for i in range(10):
    print('Linux')

# 예제 6
# 다음 형식과 같이 이름, 생년월일, 주민등록번호를 출력하는 프로그램을 작성해 보세요.
# 이름: 파이썬 생년월일: 2014년 12월 12일 주민등록번호: 20141212-1623210
name = '파이썬'
birth = '2014년 12월 12일'
id_num = '20141212-1623210'
print(f'이름: {name} 생년월일: {birth} 주민등록번호: {id_num}')

# 예제 7
# s라는 변수에 'Linux is not Unix'라는 문자열이 바인딩돼 있다고 했을 때
# 문자열의 슬라이싱 기능과 연결하기를 이용해 s의 값을
# 'Unix is not Linux'으로 변경해 보세요.
s = 'Linux is not Unix'
linux_str = s[0:5]
unix_str = s[13:]
s = f'{unix_str} is not {linux_str}'
print(s)

# 예제 8
# x라는 변수에 'abcdef'라는 문자열이 바인딩돼 있다고 했을 때
# x의 값을 'bcdefa'로 변경해 보세요.
x = 'abcdef'
a = x[0]
x = x[1:] + a
print(x)