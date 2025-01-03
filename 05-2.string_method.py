st = 'python string'

# find
print(st.find('string')) # 7

# count
print(st.count('t')) # 2

# lower
print(st.lower()) # python string

# upper
print(st.upper()) # PYTHON STRING

# replace
print(st.replace('string', '문자열')) # python 문자열

# split
print(st.split(' ')) # ['python', 'string']


st = ' python string '

# strip
print(st.strip()) # python string

# lstrip
print(st.lstrip()) # 'python string '

# rstrip
st = ' python string '
print(st.rstrip()) # ' python string'

# 예제 1
A = "Have a"
print(A)
B = " Nice Day"
C = A + B
print(C)        # Have a Nice Day
print(C*3)      # Have a Nice Day 세 번
A += " Nice Day"# A = A + " Nice Day"와 같음
print(A)        # Have a Nice Day

# 예제 2
str = "python is Easy. Programming 참 쉽죠~"
print(str)
print(str.upper())    # PYTHON IS EASY. PROGRAMMING 참 쉽죠~
print(str.lower())    # python is easy. programming 참 쉽죠~
# swapcase() 영문 소문자를 대문자로, 대문자를 소문자로 변경
print(str.swapcase()) # PYTHON IS eASY. pROGRAMMING 참 쉽죠~
# title() 단어의 시작은 대문자로 변경
print(str.title())    # Python Is Easy. Programming 참 쉽죠~