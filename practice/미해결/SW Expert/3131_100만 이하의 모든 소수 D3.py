result = []
for i in range(2, 10**6):
    for x in result:
        if i % x == 0:
            break
    ls = []
    for j in range(1, i):
        if i % j == 0:
            ls.append(j)
        if len(ls) > 1:
            break
    if len(ls) == 1:
        result.append(i)

for i in result:
    print(i, end=' ')