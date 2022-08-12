from collections import deque
r,c,k = map(int, input().split())
arry = [list(map(int, input().split())) for _ in range(3)]

def R(arr):
    arr_copy = arr.copy()
    max_len = len(arr_copy[0]) #길이가 늘어나면 0을 채워주기 위해 최대 길이를 기억
    result = []
    for row in arr_copy:
        row_dict = {}
        for num in row:
            if num == 0:
                continue
            if num in row_dict:
                row_dict[num] += 1
            else:
                row_dict[num] = 1
        row_dict = sorted(row_dict.items(), key = lambda x: (x[1], x[0]))
        row_list = []
        for item in row_dict:
            row_list.append(item[0])
            row_list.append(item[1])

        max_len = max(max_len, len(row_list))
        result.append(row_list)
    for row in result:
        if len(row) < max_len:
            for i in range(max_len - len(row)):
                row.append(0)
    return result

def C(arr: list):
    result = []
    arr_copy = arr.copy()
    row_len = len(arr_copy[0])
    max_len = len(arr_copy)
    for i in range(row_len):
        col_dict = {}
        for j in range(len(arr_copy)):
            if arr_copy[j][i] == 0:
                continue
            if arr_copy[j][i] in col_dict:
                col_dict[arr_copy[j][i]] += 1
            else:
                col_dict[arr_copy[j][i]] = 1
        col_dict = sorted(col_dict.items(), key=lambda x: (x[1], x[0]))
        col_list = []
        for item in col_dict:
            col_list.append(item[0])
            col_list.append(item[1])
        max_len = max(len(col_list), max_len)
        result.append(col_list)

    for col in result:
        if len(col) < max_len:
            for i in range(max_len - len(col)):
                col.append(0)
    return list(zip(*result))

def bfs(arr, r, c, k):
    q = deque()
    q.append((arr, 0))
    while q:
        arr_, cnt = q.popleft()
        if len(arr_)>=r and len(arr_[0]) >= c:
            if arr_[r-1][c-1] == k:
                return cnt
        if cnt >= 100:
            continue
        if len(arr_) >= len(arr_[0]):
            q.append((R(arr_), cnt+1))
        else:
            q.append((C(arr_), cnt+1))
    return -1

print(bfs(arry, r, c, k))