from bisect import bisect_left
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
name = []
value = []

for _ in range(n):
    a, b = input().split()
    name.append(a)
    value.append(int(b))

for _ in range(m):
    print(name[bisect_left(value, int(input()))])
