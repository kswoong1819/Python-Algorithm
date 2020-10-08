def solution(flowers):
    answer = 0
    days = [0] * 366
    for st, ed in flowers:
        for i in range(st, ed):
            days[i] = 1
    answer = days.count(1)
    return answer


flowers = [[2, 5], [3, 7], [10, 11]]
print(solution(flowers))
