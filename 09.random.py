from random import *

# 0.0 ~ 1.0 미만의 임의의 값 생성
print(random())

# 0.0 ~ 10.0 미만의 임의의 값 생성
print(random() * 10)

# 0 ~ 10 미만의 임의의 값 생성
print(int(random() * 10))

# 1 ~ 10 까지의 임의의 값 생성
print(int(random() * 10) + 1)

# randint()
print(randint(5, 10))  # 5 ~ 10까지의 임의의 값 생성

# randrange()
print(randrange(5, 10))  # 5 ~ 10 미만까지의 임의의 값 생성
print(randrange(5, 10, 2))  # 5부터 2씩 증가된 값에 대해 10 미만까지 임의의 값 생성

# 임의의 문자 생성
# chr() 함수
print(chr(randint(65, 90)))  # 'A' ~ 'Z'
print(chr(randint(97, 122)))  # 'a' ~ 'z'

# choice
# 주어진 시퀀스에서 무작위로 하나의 항목을 선택하여 반환한다.
menu = "순천가", "순두부찌개", "짜장면", "감자탕", "뼈해장국"
print(choice(menu))

# sample
# 주어진 시퀀스에서 중복 없이 k개의 항목을 무작위로 선택한 리스트를 반환한다.
print(sample(range(1, 47), 6))  # 1~47 사이의 숫자 6개 추첨 (복권 번호 뽑기)

# shuffle
# 주어진 시퀀스의 항목들을 무작위로 섞는다.
arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
shuffle(arr)
print(arr)

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
for i in range(3):
    print(chr(int(random() * 26) + 65))

# 예제 4
# 1 ~ 99 까지의 랜덤 값에 대해 짝수면 True,
# 홀수면 False가 나오도록 하시오
num = int(random() * 99) + 1
print(num, num % 2 == 0)

# 1. random.random()
x1 = random()
print(f"1. random.random() => {x1}")

# 2. random.uniform(a,b)
x2 = uniform(0, 1)
print(f" random.uniform(0, 1) => {x2}")

x3 = uniform(10, 20)
print(f" random.uniform(10, 20) => {x3}")

# 3. random.randint(a, b)
x4 = randint(100, 200)  # 100~200
print(f" random.randint(100, 200) => {x4}")

# 4. random.randrange(a, b) / random.randrange(b)
x5 = randrange(100, 200)  # 100~199
print(f" random.randrange(100, 200) => {x5}")

x6 = randrange(200)  # 0~199
print(f" random.randrange(200) => {x6}")

# 5. random.choice(seq)
fruits = ("apple", "pear", "pineapple")
print(f" random.choice => {choice(fruits)}")

# 6. random.sample(seq or set, N)
x8 = sample([1, 2, 3, 4, 5], 3)
print(f" random.sample([1, 2, 3, 4, 5], 3) => {x8}")

sample(range(1, 47), 6)
# 1 이상 47 미만의 6개 값을 리스트 형식으로 반환 (중복 없음)
# 시퀀스 자료형을 인자로 전달받아 임의의 값(난수)을 필요한 개수만큼
# 리스트(list)로 반환특정 영역의 숫자를 중복 없이 리턴하기 때문에 로또 번호 생성에 사용할 수 있다.

x9 = sample(range(1, 47), 6)
print(f" random.sample(range(1, 47), 6) => {x9}")

x10 = sample("aaaa", 3)  # 실제 문자가 같은지는 상관없음, index가 unique.
print(f" random.sample(aaaa, 3) => {x10}")

# 7. random.shuffle(list)
arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f" random.shuffle([1 ~ 10]) before => {arr1}")
shuffle(arr1)
print(f" random.shuffle([1 ~ 10]) after  => {arr1}")
