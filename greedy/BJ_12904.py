s = input()
t = input()
while len(s) < len(t):
    if t[-1] == 'A':
        t = t[:-1]
    else:
        t = t[:-1]
        t = "".join(reversed(t))
if s == t:
    print(1)
else:
    print(0)
