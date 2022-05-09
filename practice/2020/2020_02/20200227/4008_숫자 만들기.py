import sys
sys.stdin = open('input.txt')

def ran_oper(k, tmp):
    global max_num, min_num
    if k == N-1:
        if tmp > max_num:
            max_num = tmp
        if tmp < min_num:
            min_num = tmp
        return
    for i in range(4):
        if oper_cnt[i] > 0:
            oper_cnt[i] -= 1
            if i == 0:
                ran_oper(k + 1, tmp + nums[k+1])
            if i == 1:
                ran_oper(k + 1, tmp - nums[k+1])
            if i == 2:
                ran_oper(k + 1, tmp * nums[k+1])
            if i == 3:
                ran_oper(k + 1, int(tmp / nums[k+1]))
            oper_cnt[i] += 1

T = int(input())

for t in range(T):
    N = int(input())
    oper_cnt = list(map(int, input().split()))
    nums = list(map(int, input().split()))

    min_num = 987654321
    max_num = -987654321
    ran_oper(0, nums[0])

    print('#{} {}'.format(t + 1, max_num - min_num))
