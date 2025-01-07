from random import randint, choice

"""
반복문 for
for 변수명 in range(반복횟수):
    수행 코드
"""

# 기본 사용법
for cnt in range(10):
    print("반복 출력")

for cnt in range(10):
    print(f"{cnt}번째 반복")

# range() 함수 응용
# range(종료값)
# range(시작값, 종료값)
# range(시작값, 종료값, 증가값)
for x in range(10):
    print(x)

for x in range(5, 10):
    print(x)

for x in range(1, 10, 2):
    print(x)

# 10 9 8 7 6 5 4 3 2 1
for x in range(10, 0, -1):
    print(x, end=" ")

# range() 함수 대신 사용
for char in "abcde":
    print(char)

for tup in (1, 2, 3, 4, 5):
    print(tup)

"""
중첩 반복
for x in range(3):
    for y in range(5):
        수행 코드
    수행 코드
"""

for x in range(1, 10):
    for y in range(1, 10):
        print(x * y)

# 예제 1
# 1 ~ 20 까지의 정수 값을 출력하는 코드를 작성 하시오
for i in range(1, 20):
    print(i)

# 예제 2
# 1 ~ 20 까지의 정수 값 중 짝수에 해당하는 값 만을 출력하는
# 코드를 작성 하시오
for i in range(1, 20):
    if i % 2 == 0:
        print(i)

# 예제 3
# 100 ~ 51 까지의 정수 값 중 홀수에 해당하는 값 만을 출력하는
# 코드를 작성 하시오
# (예 – 99, 97, 95, ..., 53, 51)
for i in range(100, 51):
    if i % 2 == 1:
        print(i)

# 예제 4
# 1 ~ 50 까지의 정수 값을 출력 할 때
# 한 줄에 5개의 값이 출력 되도록 하시오
for i in range(1, 51):
    print(i, end=" ")
    if i % 5 == 0:
        print()

# 예제 5
# 1 ~ 100 까지의 누적 합을 구하는 코드를 작성 하시오
l = []
for i in range(1, 101):
    l.append(i)
print(sum(l))

# 예제 6
# 다음 문자열 변수에서 공백을 제외한 문자의 수를 구하시오
st = "Python basic program language"
num = 0
for char in st:
    if char != " ":
        num += 1
print(num)

# 예제 7
# 'a' ~ 'z' 까지 임의의 문자열을 8자리씩
# 총 10개를 생성하는 코드를 작성 하시오
# (시리얼 넘버 생성)

for serial in range(10):
    for char in range(8):
        print(chr(randint(97, 122)), end="")
    print()

# 예제 8
# 'a' ~ 'z', 'A' ~ 'Z', '0' ~ '9' 까지 임의의 문자열을
# 16자리씩 총 10개를 생성하는 코드를 작성 하시오
# (시리얼 넘버 생성)

for serial in range(10):
    for char in range(16):
        items = [randint(97, 122), randint(65, 90), randint(48, 57)]
        print(chr(choice(items)), end="")
    print()

# 예제 9
# Lotto Number generator
# 중복되지 않는 1~45까지의 숫자를 6개 추출
from random import randint

cnt = 0
lot = ""
for x in range(60):
    num = f"{randint(1, 45)}"
    if num + " " not in lot:
        lot = lot + num + " "
        cnt += 1
    if cnt == 6:
        print(lot)
        break  # 반복 종료

# 예제 10
# 구구단 출력
for i in range(1, 10):
    print(f"===== {i}단 출력 =====")
    for j in range(1, 10):
        print(f"{i} * {j} = {i * j}")
