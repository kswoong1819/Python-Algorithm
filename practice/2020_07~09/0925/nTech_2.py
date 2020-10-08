def solution(N):
    answer = 1
    n = N // 2
    for i in range(1, n + 1):
        A = 1
        for k in range(i):
            A *= (N - (i + k))
        B = 1
        for k in range(1, i + 1):
            B *= k
        answer += A // B
    return answer


N = 4
print(solution(N))
