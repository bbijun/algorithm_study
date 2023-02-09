import sys
input = sys.stdin.readline
from queue import PriorityQueue

def boj15903(arr : PriorityQueue, m):
    result = 0
    for _ in range(m):
        num1 = arr.get()
        num2 = arr.get()
        for i in range(2):
            arr.put(num1+num2)
    
    while not arr.empty():
        result += arr.get()
    return result


if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    q = PriorityQueue()
    for item in arr:
        q.put(item)
    print(boj15903(q, m))

