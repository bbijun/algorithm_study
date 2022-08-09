n = int(input())
c = list(map(int, input().split()))
k = int(input())
v = [False for _ in range(k)]
s = list(map(int, input().split()))
c = sorted(c, reverse = True)
s = sorted(s, reverse = True)

def solution():
    result = 0
    if s[0] > c[0]:
        return -1
    while False in v:
        result += 1
        for crane in c:
            for i in range(k):
                if crane >= s[i] and not v[i]:
                    v[i] = True
                    break
    return result
print(solution())