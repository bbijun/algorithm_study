def BinarySearch_Recursive(arry: list, target, start, end):
    if start > end:
        return None
    mid = (end + start)//2
    if arry[mid] == target:
        return mid
    elif arry[mid] > target:
        return BinarySearch_Recursive(arry, target, start, mid-1)
    else:
        return BinarySearch_Recursive(arry, target, mid+1, end)


def BinarySearch_Loop(arry: list, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arry[mid] == target:
            return mid
        elif arry[mid] > target:
            end = mid-1
        elif arry[mid] < target:
            start = mid + 1

#arry = [0,2,4,6,8,10,12,14,16,18]
#print(BinarySearch_Loop(arry, 4, 0, len(arry)-1))
import sys
input_data = list(map(int, sys.stdin.readline().rstrip().split()))
#test_list = list(map(int, input_data.split()))
print(input_data)