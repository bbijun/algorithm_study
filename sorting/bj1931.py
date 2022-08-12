n = int(input())
t = []
for i in range(n):
    s, e = map(int,input().split())
    t.append((s,e))
t = sorted(t, key = lambda x: (x[1], x[0]))
s = 0
result = 0
for item in t:
    if item[0]>= s:
        result+=1
        s = item[1]
print(result)