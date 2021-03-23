#동명이인 찾기
# ["Tom", "Jerry", "Mike", "Tom"] 으로 이루어진 리스트에서 같은 이름이 들어있는 집합(Set) 찾기

# 파이썬의 set : 중복을 허용하지 않고, 순서가 없음 - Java의 HashSet과 같음. 

name = ["Tom", "Jerry", "Mike", "Tom"]

def find_same(a):
    n = len(a)                  # 리스트의 길이 n
    result = set()              # 결과를 담을 set
    for i in range(0,n-1):      # 마지막 이름은 앞에서 이미 다 조회가 끝났으므로 비교할 대상이 없다. 따라서 n-1번지까지만 조회
        for j in range(i+1,n):  # j번지는 i번지는 조회할 필요가 없으므로 i번지의 다음 번지부터 조회한다.
            if a[i]==a[j]:
                result.add(a[i])
    return result

# print(find_same(name))

# n명 중 두 명을 뽑아 짝을 지을때, 짝을 지을 수 있는 모든 조합을 출력하는 알고리즘

match = ['Tom','Jerry', 'Mike']

def match_two(a):
    n = len(a)
    result = set()
    for i in range(0,n-1):
        for j in range(i+1,n):
            if a[i]!=a[j]:
                result.update(a[i],a[j])
    return result

print(match_two(match))


def pairing(a):
    n = len(a)
    for i in range(0,n-1):
        for j in range(i+1,n):
            print(a[i],'-',a[j])

pair = ['Tom','Jerry','Mike']
pairing(pair)

