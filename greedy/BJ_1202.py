from queue import PriorityQueue
n, k = map(int,input().split())
jewelry = []
for i in range(n):
    n, v = map(int, input().split())
    jewelry.append([n, v])
bags = []
for i in range(k):
    temp = int(input())
    bags.append(temp)
bags = sorted(bags) #작은 가방부터 탐색
jewelry.sort(key = lambda x:x[0]) #보석의 무게가 적은 순서대로 정렬
result = 0

for bag in bags:
    i = 0
    max_idx = 0 #가방에 담을 수 있는 보석 중 가장 값이 큰 것의 index
    max_value = 0 #가방에 담을 수 있는 보석 중 가장 값이 큰 것의 값
    while jewelry[i][0]<=bag: #보석을 순회하면서 가방에 담을 수 있는 경우
        if jewelry[i][1] > max_value: #보석의 값이 현재 max 값보다 큰 경우 값 변경
            max_idx = i
            max_value = jewelry[i][1]
        i+=1
        if i == len(jewelry):
            break
    jewelry[max_idx][1] = -1 #만약 가방이 엄청 커서 보석 전체를 순회했을 경우 while의 else를 만나지 않고 탈출하니까 이 과정 필요
    result += max_value
print(result)