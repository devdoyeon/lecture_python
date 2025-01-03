# 문자열과 정수 출력 예제
print('%s:%d'%('나이',30))
print('{} : {}'.format('나이', 30))

# 실수 출력 예제
print('%f, %.2f' % (1.123, 1.123))
print('{:f}, {:.2f}'.format(1.123, 1.123))

# 진법 출력 예제
print('%o, %x, %X' % (10, 10, 10))
print('{:b}, {:o}'.format(10, 10))
print('{:x}, {:X}'.format(10, 10))

# 고정 길이 출력
print('|%5d|' % 123)
print('|%5s|' % 'abc')
print('|{:5}|'.format(123))
print('|{:5}|'.format('abc'))

# 고정 길이의 정렬
print('|%-5d|' % 123)
print('|%5s|'.format('abc'))
print('|{:<5}|'.format(123))
print('|{:>5}|'.format('abc'))
print('|{:^5}|'.format('abc'))

# 여백 채우기
print('|%05d|' % 123)
print('|{:05}|'.format(123))
print('|{:_>5|'.format('abc'))
print('|{:-^5}|'.format('abc'))

# 정수, 실수 단위 구분
print('{:,}'.format(1000000))
print('{:,.2f}'.format(1000000))

# 예제
print('{:^70}'.format('Python Shop'))
print('{:<5}: {:<63}'.format('No.', '1078718855'))
print('{:<5}: {:<63}'.format('Addr', '서울시 종로구 종로3가'))
print('{:<5}: {:<63}'.format('Name', '김사장'))
print('{:<5}: {:<63}'.format('H.P', '070-1234-5678'))
print('-' * 70)
print('{:^20} {:^15} {:^15} {:^17}'.format('Items', 'Unit', 'QTY', 'Price'))
print('-' * 70)
print('{:^20} {:>15,} {:>15,} {:>17,}'.format('Blue-Tooth', 85000, 1, 85000))
print('{:^20} {:>15,} {:>15,} {:>17,}'.format('USB3.0 8G', 8000, 1, 8000))
print('-' * 70)
print('{:<36} {:>33,}'.format('Total', 93000))
print('-' * 70)
print('{:<36} {:>33,}'.format('Pay Money', 93000))
print('{:<36} {:>33,}'.format('Receive Money', 100000))
print('{:<36} {:>33,}'.format('Change Money', 7000))
print('-' * 70)