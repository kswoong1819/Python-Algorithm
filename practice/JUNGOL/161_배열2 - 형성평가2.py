score = map(int, input().split())

check = [0] * 11
for i in score:
    check[i // 10] += 1
check[0] -= 1

for i in range(10, -1, -1):
    if check[i] == 0:
        continue
    print('{} : {} person'.format(i * 10, check[i]))