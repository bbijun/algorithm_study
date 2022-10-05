import sys
from itertools import combinations
input = sys.stdin.readline
alphabet_dict = {}
for alphabet in range(97, 97+26):
    alphabet_dict[chr(alphabet)] = 0
alpha_set = {'a', 'n', 't', 'i', 'c'}
n, k = map(int, input().split())
wordlist = []
for _ in range(n):
    tmp = input().rstrip()
    tmp_set = set(tmp)
    for item in tmp_set:
        alphabet_dict[item] += 1
    wordlist.append(tmp_set)

if k < 5:
    print(0)
    sys.exit()

alphabets = set(alphabet_dict.keys())
alphabets -= alpha_set
combis = list(combinations(alphabets, k-5))
result = 0
for item in combis:
    set_item = set(item).union(alpha_set)
    result_tmp = 0
    for word in wordlist:
        if len(word - set_item) == 0:
            result_tmp +=1
    result = max(result_tmp, result)
print(result)