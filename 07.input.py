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

# 예제 3
# 두 정수를 입력 받아 합계를 구하는 code를 작성하세요.
s = 0
a = float(input("첫 번째 수를 입력하세요: "))
b = float(input("두 번째 수를 입력하세요: "))
s = a + b
print("두 수의 합:", s)


# 예제 4
# 두 정수를 입력 받아 합,차,평균을 구하는 code를 작성하세요.
a = float(input("첫 번째 수를 입력하세요: "))
b = float(input("두 번째 수를 입력하세요: "))
s = a + b
d = a - b
average = (a + b) / 2
print("합:", s)
print("차:", d)
print("평균:", average)


# 예제 5
# 사용자로 부터 값을 입력 받아, 평행 사변형의 면적을 구하는 code를 작성하세요.
base = float(input("밑변을 입력하세요: "))
height = float(input("높이를 입력하세요: "))
area = base * height
print("평행 사변형의 면적:", area)


# 예제 6
# 반지름값을 입력 받아 원의 면적을 구하는 code를 작성하세요.
radius = float(input("반지름값을 입력하세요: "))
area = 3.14159 * radius ** 2
print("원의 면적: ", area)

# 예제 7
# 주행한 총 마일을 입력,소비된 갤런 값을 입력을 입력 받아
# 자동차 연비를 구해보세요.
miles_driven = float(input('주행한 총 마일을 입력하세요: '))
gallons_used = float(input('소비된 갤런 값을 입력하세요: '))
print(f'자동차의 연비는 {miles_driven / gallons_used} 마일/갤런입니다.')

# 예제 8
# 가속도값과 주행시간을 입력 받아 주행 거리를 계산해 보세요.
speed = float(input('속도를 입력하세요: '))
time = float(input('주행 시간을 입력하세요: '))
print(f'주행 거리는 {speed * time}km입니다.')

# 예제 9
# 상품가격을 입력받아 부가세 10% 를 부가한 후의 상품가격을 출력하세요.
price = int(input('상품 가격을 입력하세요: '))
surtax = price * 0.1
print(f'상품 가격은 {format(int(price + surtax), ',')}원입니다.')

# 예제 10
# 상품가격, 할인율을 입력받아 최종 상품 가격을 출력하세요.
price = int(input('상품 가격을 입력하세요: '))
sale = 1 - int(input('할인율을 입력하세요: ')) / 100
print(f'상품 가격은 {format(int(price * sale), ',')}원입니다.')

# 예제 11
# 상품가격, 할인율 입력 받고, 할인이 적용된 상품값에 부가세 10%를 적용한
# 최종 상품가격을 출력하세요.
price = int(input('상품 가격을 입력하세요: '))
sale = 1 - int(input('할인율을 입력하세요: ')) / 100
surtax = (price * sale) * 0.1
print(f'최종 상품 가격은 {format(int(price * sale + surtax))}원입니다.')