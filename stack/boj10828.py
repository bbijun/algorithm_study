import sys
input = sys.stdin.readline

def boj10828():
    n = int(input())
    stack = []
    for _ in range(n):
        com = input().rstrip()
        if len(com) > 5:
            com_first, num = com.split()
            stack.append(int(num))

        elif com == "top":
            if len(stack) == 0:
                print(-1)
            else:
                print(stack[-1])
        
        elif com == "size":
            print(len(stack))
        
        elif com == "pop":
            if len(stack) == 0:
                print(-1)
            else:
                print(stack.pop())
        
        else:
            print(1) if len(stack) == 0 else print(0)

if __name__ == "__main__":
    boj10828()

            
        
