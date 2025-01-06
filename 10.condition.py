# 조건 - Boolean
'''
if 조건식:
    수행 코드
'''
if True:
    print('a')

if False:
    print('b')

# 조건 - 비교 연산자
x = 15
if x > 10:
    print('x는 10보다 크다.')

# 조건 - 멤버 연산자
x = 15
if x in (10, 11, 12):
    print('x는 10, 11, 12 중 하나에 포함된다.')

# 조건 - 식별 연산자
x = 15
if type(x) is int:
    print('x는 int형 자료이다.')

# 조건 - 비교, 논리 연산자
x = 15
if x > 10 and x != 15:
    print('x는 10보다 크면서 15는 아니다.')

'''
if ... else문
if 조건식:
    수행 코드
else:
    수행 코드
'''

number = int(input('정수 값 입력: '))
if number % 3 == 0:
    print('3의 배수이다.')
else:
    print('3의 배수가 아니다.')

# 예제 1
# 사용자로부터 정수 값을 입력 받고 입력 받은 값이
# 짝수 또는 홀수 인지를 구분하는 코드를 작성하시오
number = int(input('정수 값을 입력하세요: '))
if number % 2 == 0:
    print('짝수입니다.')
else:
    print('홀수입니다.')

# 예제 2
# 사용자로부터 2개의 정수 값을 입력 받아 빼기 계산을 할 때
# 항상 양의 정수가 나올 수 있도록 하시오
num1 = int(input('정수 값을 입력하세요: '))
num2 = int(input('정수 값을 입력하세요: '))
if num1 > num2:
    print(num1 - num2)
else:
    print(num2 - num1)

# 예제 3
# 사용자로부터 2개의 정수 값을 입력 받고 홀, 짝을 비교하였을 때
# 2개의 값이 전부 홀수 또는 짝수이면, 2개의 정수 값을 더하고
# 2개의 값이 홀-짝 또는 짝-홀이면, 2개의 정수 값을 곱하시오
num1 = int(input('정수 값을 입력하세요: '))
num2 = int(input('정수 값을 입력하세요: '))
if num1 % 2 == 0 and num2 % 2 == 0 or num1 % 2 != 0 and num2 % 2 != 0:
    print(num1 + num2)
else:
    print(num1 * num2)

# 예제 4
# 랜덤 함수를 통해 생성 된 2개의 값(10 ~ 99 까지)으로 더하기 문제를 만들고
# 만들어진 문제를 사용자가 풀어보는 형식의 코드를 작성하시오
from random import randint
rand1 = randint(10, 99)
rand2 = randint(10, 99)
plus = input(f'{rand1} + {rand2} = ')
if int(plus) == rand1 + rand2:
    print('정답입니다.')
else:
    print('오답입니다.')