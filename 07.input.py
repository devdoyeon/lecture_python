# 사용자 입력 값 받기
input('값을 입력하시오: ')

# 사용자 입력값 변수에 저장
userin = input('값을 입력하시오: ')

# 사용자 입력값의 자료형
userin = input('값 입력: ')
print(type(userin)) # <class 'str'>

age = input('나이: ')
name = input('이름: ')
print('{}님의 나이는 {}세 입니다.'.format(name, age))

# 예제 1
# input()으로 2개의 값을 받은 다음 더하기, 빼기, 곱하기,
# 나누기 연산을 하여 그 결과를 출력하는 코드를 작성하시오
one = input('첫 번째 숫자: ')
two = input('두 번째 숫자: ')
one_int = int(one)
two_int = int(two)
print(f'더하기: {one_int + two_int}, 빼기: {one_int - two_int}, 곱하기: {one_int * two_int}, 나누기: {one_int / two_int}')

# 예제 2
# 사용자로부터 이름, 키, 체중 값을 입력 받아 비만도를 구하고
# 출력하는 코드를 작성하시오
# 비만도 계산 식 : 비만도(%) = 현재 체중 / 표준 체중 * 100
# 표준 체중 계산 식 : 표준 체중 = (현재 키 – 100) * 0.9
# 출력 예제 : 홍길동님의 비만도는 112.15% 입니다.
name = input('이름: ')
height = input('키: ')
weight = input('체중: ')
standard_weight = (int(height) - 100) * 0.9
print(f'{name}님의 비만도는 {round(int(weight) / standard_weight * 100, 2)}%입니다.')