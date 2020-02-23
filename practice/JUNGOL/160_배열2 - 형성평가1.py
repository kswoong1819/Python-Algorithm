nums = map(int, input().split())

check = [0] * 7

for i in nums:
    check[i] += 1

for i in range(1, 7):
    print('{} : {}'.format(i, check[i]))