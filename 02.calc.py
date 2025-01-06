# max(), min()
print(max(3, 7, -1, 5, 4))  # 7
print(min(3, 7, -1, 5, 4))  # -1

# sum() = 모두 더한 값
# pow() = 제곱
print(sum([2, 4, 6, 8, 10]))  # 30
print(pow(2, 3))  # 8 = 2^3
print(pow(3, 3))  # 27 = 3^3

# divmod() = 몫과 나머지
print(divmod(10, 3))  # (3, 1) => 10 / 3 = 몫 3, 나머지 1
print(divmod(10, 2))  # (5, 0)

# round() = 반올림
print(round(11.56, 1))  # 11.6
print(round(11.12, 1))  # 11.1
print(round(5 / 3, 3))  # 1.667

# abs() = 절댓값
print(abs(-5))  # 5

# 예제
print(max(32, 45, 48, 57, 84), min(32, 45, 48, 57, 84))
arr = [29, 95, 15, 85, 66]
print(sum(arr))
print(sum(arr) / 5)
print(divmod(sum(arr), 5))
print(pow(max(3, 4, 8, 5), min(3, 4, 8, 5)))
