tmp = 1
for i in range(3):
    num = int(input())
    tmp *= num

total = str(tmp)
check = [0] * 10

for i in total:
    check[int(i)] += 1

for i in range(10):
    print(check[i])
