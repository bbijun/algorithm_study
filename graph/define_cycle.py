def find_parent(parent, x):
    #find root using recursive func
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

v, e = map(int, input().split()) #nodes, edges num
parent = [0] * (v+1)
for i in range(v+1):
    parent[i] = i

cycle = False #is there's cycle

for _ in range(e):
    a, b = map(int, input().split())
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    else:
        union_parent(parent, a, b)

if cycle:
    print('Cycle found')
else:
    print('No cycle found')