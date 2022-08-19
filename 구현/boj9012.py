import sys
input = sys.stdin.readline
n = int(input())
def check(str):
    stack = []
    for char in str:
        if char == '(':
            stack.append(char)
        else:
            if len(stack) > 0:
                stack.pop()
            else:
                return 'NO'
    if len(stack) > 0:
        return 'NO'
    else:
        return 'YES'

for _ in range(n):
    print(check(input().strip()))