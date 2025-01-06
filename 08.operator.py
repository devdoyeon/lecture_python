num1, num2, num3 = 5, 15, 27
# 위 변수에 할당된 값을 사용하여 다음의 결과가 나오도록
# 산술 연산자를 사용 하시오.

# ㄱ. -12
# ㄴ. 75
# ㄷ. 25
# ㄹ. 5.4
# ㅁ. 3.0

print(num2 - num3)  # -12
print(num1 * num2)  # 75
print(num1 * num1)  # 25
print(num3 / num1)  # 5.4
print(num2 / num1)  # 3.0

# 다음의 연산자를 보고 True와 False를 구분 하시오
# ㄱ. 7 > 18 # False
# ㄴ. 5 < 2 # False
# ㄷ. 6 % 3 > 2 # False
# ㄹ. 5 + 5 != 2 * 5 # False
# ㅁ. True == 1 # True
# ㅂ. 1 == '1' # False
# ㅅ. 10 // 3 == 10 % 3 # False
# ㅇ. 15 % 4 in (0, 1, 2) # False

# a 가 짝수인 조건 만들기
a = 10
if a % 2 == 0:
    print("Even")
else:
    print("Odd")

# a를 2로 나누어 0이면 false이고, not이면 True 의미
a = 10
if not a % 2:
    print("Even")
else:
    print("Odd")

# a 가 홀수인 조건 만들기
a = 9
if a % 2 == 1:
    print("Odd")
else:
    print("Even")

# a를 2로 나누어 0이면 false이고, not이면 True 의미
a = 9
if a % 2:
    print("Odd")
else:
    print("Even")

# a 가 3의 배수인 조건 만들기
# a를 3로 나누어 0이면 false이고, not이면 True 의미
a = 9
if not a % 3:
    print("3배수")
else:
    print("배수 아님")

a = 15
if 10 < a < 20:
    print("10 < a < 20")
else:
    print("Not 10 < a < 20")

a, b = 0, 1
if type(a) is int and type(b) is int:
    print("a and b int all")
else:
    print("a and b not int all")

a, b = 0, 1
if type(a) is int and type(b) is not int:
    print("a and b int all")
else:
    print("a and b not int all")
