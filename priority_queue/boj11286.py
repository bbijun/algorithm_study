import sys
input = sys.stdin.readline
from queue import PriorityQueue

def boj11286():
    n = int(input())
    q = PriorityQueue()
    for _ in range(n):
        a = int(input())
        if a == 0:
            if q.empty():
                print(0)
            else:
                num, x = q.get()
                print(num * x)
        elif a>0:
            q.put((a,1))
        else:
            q.put((-a, -1))

if __name__ == "__main__":
    boj11286()
