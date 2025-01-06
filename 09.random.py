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