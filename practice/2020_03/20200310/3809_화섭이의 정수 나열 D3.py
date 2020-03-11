import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(T):
    N = int(input())
    nums = []
    while len(nums) < N:
        nums += list(map(int, input().split()))
    check = [0] * 1000

    for i in range(1, 4):
        for j in range(0, N-i+1):
            a = ''
            for z in range(j, j+i):
                a += str(nums[z])
            check[int(a)] = 1

    for i in range(1000):
        if check[i] == 0:
            print('#{} {}'.format(t+1, i))
            break