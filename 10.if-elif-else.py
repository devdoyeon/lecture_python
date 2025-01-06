# 조건 - Boolean
"""
if 조건식:
    수행 코드
"""
if True:
    print("a")

if False:
    print("b")

# 조건 - 비교 연산자
x = 15
if x > 10:
    print("x는 10보다 크다.")

# 조건 - 멤버 연산자
x = 15
if x in (10, 11, 12):
    print("x는 10, 11, 12 중 하나에 포함된다.")

# 조건 - 식별 연산자
x = 15
if type(x) is int:
    print("x는 int형 자료이다.")

# 조건 - 비교, 논리 연산자
x = 15
if x > 10 and x != 15:
    print("x는 10보다 크면서 15는 아니다.")

"""
if ... else문
if 조건식:
    수행 코드
else:
    수행 코드
"""

number = int(input("정수 값 입력: "))
if number % 3 == 0:
    print("3의 배수이다.")
else:
    print("3의 배수가 아니다.")

# 예제 1
# 사용자로부터 정수 값을 입력 받고 입력 받은 값이
# 짝수 또는 홀수 인지를 구분하는 코드를 작성하시오
number = int(input("정수 값을 입력하세요: "))
if number % 2 == 0:
    print("짝수입니다.")
else:
    print("홀수입니다.")

# 예제 2
# 사용자로부터 2개의 정수 값을 입력 받아 빼기 계산을 할 때
# 항상 양의 정수가 나올 수 있도록 하시오
num1 = int(input("정수 값을 입력하세요: "))
num2 = int(input("정수 값을 입력하세요: "))
if num1 > num2:
    print(num1 - num2)
else:
    print(num2 - num1)

# 예제 3
# 사용자로부터 2개의 정수 값을 입력 받고 홀, 짝을 비교하였을 때
# 2개의 값이 전부 홀수 또는 짝수이면, 2개의 정수 값을 더하고
# 2개의 값이 홀-짝 또는 짝-홀이면, 2개의 정수 값을 곱하시오
num1 = int(input("정수 값을 입력하세요: "))
num2 = int(input("정수 값을 입력하세요: "))
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
plus = input(f"{rand1} + {rand2} = ")
if int(plus) == rand1 + rand2:
    print("정답입니다.")
else:
    print(f"오답입니다. 정답은 {rand1 + rand2}입니다.")

# 예제 5
# 계정 생성 프로그램을 작성 하시오.
# 1. 사용자로 부터 계정을 생성하기 위한 ID와 PW를 입력 받습니다.
# 2. PW의 경우 한번 더 사용자 입력을 받아서 이전에 입력한 PW와 일치
# 한 PW를 입력 하였는지를 확인하여 일치한 경우에만 "계정 생성 완료"
# 메시지를 출력하고 그렇지 않은 경우에는 "계정 생성 실패" 메시지
# 를 출력하게 하시오.

id_input = input("ID를 입력하세요: ")
pw_input = input("PW를 입력하세요: ")
pw_chk = input("PW를 다시 한 번 입력하세요: ")
if pw_input == pw_chk:
    print("계정 생성 완료")
else:
    print("계정 생성 실패")

# 예제 6
# 10 ~ 99 까지 임의의 값 2개를 생성하고 나누기 계산을
# 할 때 '큰값 / 작은값'의 형태가 되도록 코드 작성
one = randint(10, 99)
two = randint(10, 99)
print(one, two)
if one > two:
    print(one / two)
else:
    print(two / one)

"""
if ... elif ... else문
if 조건식:
    수행 코드
elif 조건식:
    수행 코드
else:
    수행 코드
"""
score = int(input("점수 입력 : "))
if 90 <= score <= 100:
    print("수 입니다.")
elif 80 <= score < 90:
    print("우 입니다.")
elif 70 <= score < 80:
    print("미 입니다.")
elif 60 <= score < 70:
    print("양 입니다.")
else:
    print("가 입니다.")

"""
중첩 if문
if 조건식:
    if 조건식:
        수행 코드
    수행 코드
else:
    수행 코드
"""
score = int(input("점수 입력 : "))
if 0 <= score <= 100:
    if 90 <= score <= 100:
        print("수 입니다.")
    elif 80 <= score < 90:
        print("우 입니다.")
    elif 70 <= score < 80:
        print("미 입니다.")
    elif 60 <= score < 70:
        print("양 입니다.")
    else:
        print("가 입니다.")
else:
    print("잘못된 입력값 입니다.")

# 예제 1
# 사용자로부터 이름, 키, 체중 값을 입력 받아 비만도를 구하고
# 결과를 출력 할 때 비만도 값 100을 기준으로 100 미만이면
# 저체중, 100 이상 110 미만은 정상, 110 이상 120 미만 과제중,
# 120 이상 130 미만 비만, 130 이상은 고도비만으로 출력 하시오
# 비만도 계산 식 : 비만도(%) = 현재 체중 / 표준 체중 * 100
# 표준 체중 계산 식 : 표준 체중 = (현재 키 – 100) * 0.9
# 출력 예제 : 홍길동님의 비만도는 112.15% 로 과체중 입니다.
name = input("이름: ")
height = int(input("키: "))
weight = int(input("체중: "))

standard_weight = (height - 100) * 0.9
obesity = round(weight / standard_weight * 100, 2)
str = ""
if obesity < 100:
    str = "저체중"
elif 100 <= obesity < 110:
    str = "정상"
elif 110 <= obesity < 120:
    str = "과체중"
elif 120 <= obesity < 130:
    str = "비만"
else:
    str = "고도비만"
print(f"{name}님의 비만도는 {obesity}%로 {str}입니다.")

# 예제 2
# 윤년을 구하는 코드를 작성 하시오
# - 4의 배수는 윤년이 된다. 그 외는 평년
# - 4의 배수 면서 100의 배수인 경우는 평년이다. 그 외는 윤년
# - 4 그리고 100의 배수이면서 400의 배수인 경우 윤년이다.
# 그 외는 평년
# 출력 예제 : 2017년은 평년 입니다.
year = int(input("연도를 입력해 주세요: "))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f"{year}년은 윤년입니다.")
else:
    print(f"{year}년은 평년입니다.")

# 예제 3
"""
            2018년 5월
Sun. Mon. Tue. Wed. Thu. Fri. Sat.
             1    2    3    4    5
   6    7    8    9   10   11   12
  13   14   15   16   17   18   19
  20   21   22   23   24   25   26
  27   28   29   30   31
"""
# 위의 달력 형태를 보고 사용자가 입력하는 날짜 값에 맞는 요일을 출력하시오.
# 입력 예제
# 일자 : 10
# 일자 : 35
# 출력 예제
# 10일은 목요일(Thu.) 입니다.
# 입력 값의 범위를 벗어났습니다.
day = int(input("일자: "))
if 1 <= day <= 31:
    if day % 7 == 1:
        print(f"{day}일은 화요일(Tue.) 입니다.")
    elif day % 7 == 2:
        print(f"{day}일은 수요일(Wed.) 입니다.")
    elif day % 7 == 3:
        print(f"{day}일은 목요일(Thu.) 입니다.")
    elif day % 7 == 4:
        print(f"{day}일은 금요일(Fri.) 입니다.")
    elif day % 7 == 5:
        print(f"{day}일은 토요일(Sat.) 입니다.")
    elif day % 7 == 6:
        print(f"{day}일은 일요일(Sun.) 입니다.")
    elif day % 7 == 0:
        print(f"{day}일은 월요일(Mon.) 입니다.")
else:
    print("입력 값의 범위를 벗어났습니다.")
