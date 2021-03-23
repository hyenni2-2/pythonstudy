# 모두의 알고리즘 1-1 제곱의 합 구하기

def for_test(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum + (i * i)
    return sum

print(for_test(10))


# 제곱근의 합 수학공식
def for_sum(a):
    return a * (a + 1) * (2 * a + 1) // 6

print(for_sum(10))

    


