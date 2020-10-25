def solution(p, n):
    a, tm = p.split()
    time = list(map(int, tm.split(':')))
    time[2] += n
    if a == "PM":
        time[0] += 12
    for i in range(2, 0, -1):
        tmp = time[i] // 60
        time[i] %= 60
        time[i - 1] += tmp
    tmp = time[0] // 24
    time[0] -= 24 * tmp
    if a == 'AM' and (int(time[1]) > 0 or int(time[2]) > 0):
        time[0] -= 12
    elif a == 'AM' and not (int(time[1]) > 0 or int(time[2]) > 0):
        if time[0] == 0:
            time[0] = 12
    for i in range(3):
        tt = str(time[i])
        if len(tt) == 1:
            tt = '0' + tt
        time[i] = tt
    answer = ':'.join(time)
    return answer


p = "AM 01:00:00"
n = 3600
# p = "AM 10:59:59"
# n = 11
print(solution(p, n))
