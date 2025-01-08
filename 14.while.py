# """
# 기본 사용법
# while 조건문:
#     수행 코드
# """
# from pickletools import TAKEN_FROM_ARGUMENT4
#
# # 비교 연산자 사용
# x = 0
# while x < 3:
#     x += 1
#
# # 멤버 연산자 사용
# x = 0
# while x in (0, 1, 2):
#     x += 1
#
# # 무한 반복
# x = 0
# while True:
#     print(x)
#     x += 1
#
# # 반복의 종료
# x = 0
# while True:
#     if x % 2 == 0:
#         break
#     print(x)
#     x += 1
#
# # 반복의 처음으로 이동
# x = 0
# while True:
#     if x % 2 == 0:
#         continue
#     print(x)
#     x += 1
#
# # 중첩 반복문의 break, continue
# x = 0
# while True:
#     while True:
#         if x == 5:
#             y += 1
#             break
#         x += 1
#
# x = 0
# while True:
#     while True:
#         if x == 5:
#             y += 1
#             continue
#         x += 1

# 예제 1
# 1 ~ 20 까지의 정수 값을 출력하는 코드를 작성 하시오
# (while 문으로만 작성)
x = 0
while True:
    if x == 20:
        break
    x += 1
    print(x)

# 예제 2
# 1 ~ 100 까지의 누적 합을 구하는 코드를 작성 하시오
# (while 문으로만 작성)
sum = 0
i = 1
while i < 101:
    sum += i  # sum = sum + i
    i += 1
print(sum)

# 예제 3
# 사용자가 입력한 값을 초과하지 않는 한도에서의
# 누적 합을 구하는 코드를 작성 하시오
# (누적 합은 랜덤으로 1~10 까지 생성)
guess = int(input("값을 입력하세요: "))
lst = []
cnt = 0
while True:
    cnt += 1
    lst.append(cnt)
    if guess == cnt:
        break
print(sum(lst))

# 예제 4
# 사용자가 입력한 정수 값에 대해 2진수로 변환하여 출력하는
# 코드를 작성 하시오
while True:
    input = int(input("정수값을 입력하세요: "))
    print(bin(input))

# 예제 5
# 로또 번호 6개 생성 할 때 중복 없이 6개 생성
from random import randint

cnt = 0
lot = ""
while cnt < 6:
    rand = randint(1, 45)
    if str(rand) not in lot:
        lot = lot + "{:02} ".format(rand)
        cnt = cnt + 1
print(lot)

# 예제 6
# 윤년 구하기
year = 0
cnt = 0
while True:
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(f"{year}년은 윤년입니다.")
                cnt = cnt + 1
            if year == 3000:
                break
        else:
            print(f"{year}년은 평년입니다.")
            cnt += 1
    year += 1

# 예제 7
# 구구단
i = 1
while i < 10:
    print()
    print(f"**** {i}단 ****")
    j = 1
    while j < 10:
        print(f"{i} * {j} = {i * j}")
        j += 1
    i += 1
