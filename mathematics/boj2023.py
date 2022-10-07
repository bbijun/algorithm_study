def is_prime_number(x):
    if x == 0 or x == 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

n = int(input())
check_list = {}
num = 10**(n-1)
while num < 10**(n)+1:
    flag = True
    for k in range(n-1,-1,-1):
        tmp = num // 10**k
        if tmp not in check_list:
            check_prime = is_prime_number(tmp)
            check_list[tmp] = check_prime
            if not check_prime:

                flag = False
                break
        else:
            if not check_list[tmp]:

                flag = False
                break
    if flag:print(num)
    num+=1
