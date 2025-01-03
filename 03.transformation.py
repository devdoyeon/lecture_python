# 진법 변환
# bin(Binary) 2진수 값으로 변환
# oct(Octal) 8진수 값으로 변환
# hex(Hexadecimal) 16진수 값으로 변환

# int(Integer) 10진수 값으로 변환
# int(0x1A, 16) => 16진수인 0x1A라는 값을 10진수로 변환

print(bin(100)) # 0b110010
print(oct(100)) # 0o144
print(hex(100)) # 0x64

print(bin(0b100)) # 0b100
print(oct(0b100)) # 0o4
print(hex(0b100)) # 0x4

print(bin(0x1A)) # 0b11010
print(oct(0x1A)) # 0o32
print(hex(0x1A)) # 0x1A

print(bin(4 + 4)) # 0b1000
print(oct(0xA + 0xB)) # 0o25
print(hex(0b10 * 5)) # 0xA

# 예제
print(int(0x3d5f)) # 15711
print(hex(1024)) # 0x400
print(bin(0x35)) #0b110101
print(hex(0o35)) # 0x1d
print(hex(3452+5785)) # 0x2415
print(bin(0xAC+ 200)) # 0b101110100