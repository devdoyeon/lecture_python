from random import random, randint, randrange

# 0.0 ~ 1.0 미만의 임의의 값 생성
print(random())

# 0.0 ~ 10.0 미만의 임의의 값 생성
print(random() * 10)

# 0 ~ 10 미만의 임의의 값 생성
print(int(random() * 10))

# 1 ~ 10 까지의 임의의 값 생성
print(int(random() * 10) + 1)

# randint()
print(randint(5, 10)) # 5 ~ 10까지의 임의의 값 생성

# randrange()
print(randrange(5, 10)) # 5 ~ 10 미만까지의 임의의 값 생성
print(randrange(5, 10, 2)) # 5부터 2씩 증가된 값에 대해 10 미만까지 임의의 값 생성

# 임의의 문자 생성
# chr() 함수
print(chr(randint(65, 90))) # 'A' ~ 'Z'
print(chr(randint(97, 122))) # 'a' ~ 'z'

# 예제 1
# 1 ~ 100 까지 랜덤 값을 출력하는 코드를 작성하시오
# (단, randint(), randrange()는 사용 하지 않음)
print(int(random() * 100) + 1)

# 예제 2
# 100 ~ 999 까지 랜덤 값을 출력하는 코드를 작성하시오
# (단, randint(), randrange()는 사용 하지 않음)
print(int(random() * 999) + 100)

# 예제 3
# 'A' ~ 'Z' 까지 임의의 문자 3자리를 출력하는 코드를 작성하시오
# (단, randint(), randrange()는 사용 하지 않음)
print(chr(int(random() * 26) + 65), chr(int(random() * 26) + 65), chr(int(random() * 26) + 65))

# 예제 4
# 1 ~ 99 까지의 랜덤 값에 대해 짝수면 True,
# 홀수면 False가 나오도록 하시오
num = int(random() * 99) + 1
if num % 2 == 0:
    print(True)
else:
    print(False)