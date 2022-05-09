import sys
sys.stdin = open('input.txt', 'r')

'''
for t in range(10):
    case = input()
    matrix = [list(map(int, input().split())) for _ in range(100)]
    list_sum = []

    for i in range(100):
        x_sum = y_sum = z_sum = 0
        for j in range(100):
            x_sum += matrix[i][j]
            y_sum += matrix[j][i]
            if i == j:
                z_sum += matrix[i][j]
        list_sum.append(x_sum)
        list_sum.append(y_sum)
        list_sum.append(z_sum)

    max_num = list_sum[0]
    for n in range(1, len(list_sum)):
        if max_num < list_sum[n]:
            max_num = list_sum[n]
    print('#{} {}'.format(t+1,max_num))
''' # 내 풀이

'''
for tc in range(10):
    tc_num = int(input())

    nums = [0] * 100
    for i in range(len(nums)):
        nums[i] = list(map(int, input().split()))

    maxSum = 0

    # 행의 합
    for i in range(len(nums)):
        sum1 = 0
        for j in range(len(nums)):
            sum1 += nums[i][j]
        if sum1 > maxSum:
            maxSum = sum1

    # 열의 합
    for i in range(len(nums)):
        sum2 = 0
        for j in range(len(nums)):
            sum2 += nums[j][i]
        if sum2 > maxSum:
            maxSum = sum2

    # 대각합
    sum3 = 0
    sum4 = 0
    for i in range(len(nums)):
        sum3 += nums[i][i]
        sum4 += nums[i][len(nums) - 1 - i]

    if sum3 > maxSum:
        maxSum = sum3
    if sum4 > maxSum:
        maxSum = sum4

    print("#{} {}".format(tc_num, maxSum)
''' # 강사님 풀이