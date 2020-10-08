def solution(ball, order):
    answer = []
    i = 0
    while len(ball) > 0:
        n = order[i]
        if ball[0] == n or ball[-1] == n:
            ball.remove(n)
            order.remove(n)
            answer.append(n)
            i = 0
        else:
            i += 1
    return answer


# ball = [1, 2, 3, 4, 5, 6]
# order = [6, 2, 5, 1, 4, 3]

ball = [11, 2, 9, 13, 24]
order = [9, 2, 13, 24, 11]

print(solution(ball, order))
