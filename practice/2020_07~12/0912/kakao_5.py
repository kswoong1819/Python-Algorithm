def solution(play_time, adv_time, logs):
    st = 400000
    ed = 0
    L = calcul(play_time)
    check = []
    A = calcul(adv_time)
    for log in logs:
        x, y = log.split('-')
        a = calcul(x)
        b = calcul(y)
        if st > a:
            st = a
        if ed < b:
            ed = b
        check.append([0]*(a-1) + [1]*(b-a+1) + [0]*(b-1))

    max_time = 0
    idx = 0
    for i in range(st, ed-A):
        tmp = 0
        for j in range(len(logs)):
            tmp += sum(check[j][i:i + A])
        if max_time < tmp:
            max_time = tmp
            idx = i
    answer = decal(idx)
    return answer


def calcul(t):
    H, M, S = t.split(':')
    S = int(S)
    S += int(M) * 60
    S += int(H) * 60 * 60
    return S


def decal(t):
    H = t // 3600
    t = t % 3600
    M = t // 60
    S = t % 60
    T = [H, M, S]
    for i in range(3):
        I = str(T[i])
        if len(I) == 0:
            T[i] = '00'
        elif len(I) == 1:
            T[i] = '0' + I
        else:
            T[i] = I
    return '{}:{}:{}'.format(T[0], T[1], T[2])


# play_time = "02:03:55"
# adv_time = "00:14:15"
# logs = ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]

play_time = "99:59:59"
adv_time = "25:00:00"
logs = ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]

# play_time = "50:00:00"
# adv_time = "50:00:00"
# logs = ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]

print(solution(play_time, adv_time, logs))
