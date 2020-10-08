def solution(n):
    global result_cnt, result
    N = str(n)
    if len(N) == 1:
        return [0, n]
    result_cnt = 999999
    result = 0
    tracking(N, 0)
    return [result_cnt, result]


def tracking(num, k):
    global result_cnt, result
    if result_cnt <= k:
        return
    while len(num) != 1:
        for d in range(1, len(num)):
            while 1:
                a = num[:d]
                b = num[d:]
                if len(a) == 0 or len(b) == 0:
                    break
                if a[0] == '0' or b[0] == '0':
                    d += 1
                else:
                    N = str(int(a) + int(b))
                    tracking(N, k + 1)
                    break
        else:
            return
    if len(num) == 1:
        if result_cnt > k:
            result_cnt = k
            result = int(num)
        return


# n = 73425
# n = 10007
n = 9

print(solution(n))
