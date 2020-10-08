m = "kkaxbycyz"
k = "abc"
a = list(m)
tmp = 0
for i in k:
    for j in range(tmp, len(m)):
        if i == a[j]:
            a.pop(j)
            tmp = j
            break

print(''.join(a))