# 숫자 n개를 리스트로 입력받아서 최솟값 구하기

def find_min(a): 
    n=len(a)     #n은 a라는 리스트의 길이
    min_idx=0    #최솟값의 idx를 저장할 변수 min_idx
    for i in range(0,n):
        if a[i]<a[min_idx]:
            min_idx=i
    return a[min_idx]

b=[9,23,30,100,36,2,1,32]

print(find_min(b))


