X = int(input())
ls = []
n = 0
ans = len(ls)
while ans <= X:
    ans = len(ls)
    n += 1
    if n % 2 != 0:
        for i in range(n):
            ls.append(str(n - i) + '/' + str(i + 1))
    else:
        for i in range(n):
            ls.append(str(i + 1) + '/' + str(n - i))
print(ls[X - 1])
