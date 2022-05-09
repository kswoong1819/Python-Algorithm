def solution(n):
    answer = []
    dr = [1, 0, -1]
    dc = [0, 1, -1]
    snail = [[0] * n for _ in range(n)]
    snail[0][0] = 1
    end_num = sum(k for k in range(n + 1))
    r, c = 0, 0
    num = 1
    while num != end_num:
        for i in range(3):
            while 1:
                nr = r + dr[i]
                nc = c + dc[i]
                if nr < 0 or nr >= n or nc < 0 or nc >= n:
                    break
                if snail[nr][nc] != 0:
                    break
                num += 1
                snail[nr][nc] = num
                r, c = nr, nc
    for i in range(n):
        answer.extend(snail[i][:i + 1])
    return answer


n = 4
print(solution(n))
