n = 19
edges = [[0, 1], [0, 2], [0, 3], [1, 4], [1, 5], [2, 6], [3, 7], [3, 8], [3, 9], [4, 10], [4, 11], [5, 12], [5, 13], [6, 14], [6, 15], [6, 16], [8, 17], [8, 18]]


def go(st):
    global a, b
    check = []
    c = 0
    while st:
        n, cnt = st.pop()
        c = cnt + 1
        for ed in q[n]:
            check.append([ed[1], cnt+1])
    if len(check) == 0 or len(check) == 1:
        a.append(c)
        return
    for i in range(len(check)):
        tmp = check.copy()
        tmp.pop(i)
        go(tmp)

q = [[] for _ in range(n)]
for a, b in edges:
    q[a].append([a, b])

st = [0]
b = 0
a = []
go([[0, 0]])

print(a)
