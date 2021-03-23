# 1-1 정수를 입력받아 세 정수의 최댓값 구하기

print('세 정수를 입력하세요.')
a = int(input('정수 a의 값을 입력하세요.: '))
b = int(input('정수 b의 값을 입력하세요.: '))
c = int(input('정수 c의 값을 입력하세요.: '))

max = a
if b > max :
    max = b
if c > max: 
    max = c

print(f'최댓값은 {max}입니다.')

# 보충 1-1 문자열, 숫자 입력받기
print('이름을 입력하세요.: ', end='')
name = input()
print(f'안녕하세요? {name} 님.')
