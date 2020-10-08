def solution(N, stages):
    answer = []
    P = len(stages)
    rating = []
    for i in range(1, N + 1):
        if P == 0:
            rate = 0
        else:
            rate = stages.count(i) / P
        rating.append([i, rate])
        P -= stages.count(i)

    rating = sorted(rating, key=lambda x: x[1], reverse=True)

    for i in range(N):
        answer.append(rating[i][0])
    return answer


N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
# N = 4
# stages = [4,4,4,4,4]

print(solution(N, stages))
