# a부터 b까지 정수의 합을 구하기(for문)위해 값 정렬

print('a부터 b까지 정수의 합을 구합니다.')
a = int(input('정수 a를 입력하세요.: '))
b = int(input('정수 b를 입력하세요.: '))

if a > b:
    a, b = b, a

sum = 0
for i in range(a, b + 1):
    sum += i

print(f'{a}부터 {b}까지 정수의 합은 {sum}입니다.')


# +와 -를 번갈아가며 출력하기(내 코드)
print('+와 -를 번갈아 출력합니다.')
n = int(input('몇 개를 출력할까요? : '))

for i in range(1,n + 1):
    if i % 2:
        print('+',end='')
    else:
        print('-',end='')

print()

# +와 -를 번갈아가며 출력하기(교재 코드)
print('+와 -를 번갈아 출력합니다.')
n = int(input('몇 개를 출력할까요? : '))

for _ in range(n // 2):
    print('+-',end='')

if n % 2:
    print('+', end='')

print()

