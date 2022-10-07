def is_prime_number(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


n = int(input())
check = [[False, False] for _ in range(10**n + 1)]
flag = True

for num in range(10**(n-1), 10**(n)-1):#10**(n-1),10**n - 1
    flag = True
    for k in range(n-1, -1, -1):
        tmp = (num // 10 ** k)
        if not check[tmp][0]:
            check[tmp][0] = True
            if is_prime_number(num):
                check[tmp][1] = True
            else:
                flag = False
                break
        else:
            if not check[tmp][1]:
                flag = False
                break
    if flag:
        print(num)
    print(num)