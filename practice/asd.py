def solution(board):
    answer = 0
    for i in range(len(board[0])):
        cnt = 0
        for j in range(len(board)):
            if board[i][j] == 1:
                cnt += 1
                tmp = 0
                for k in range(i, i+cnt):
                    if board[k][j] == 1:
                        tmp += cnt
                answer = max(answer, tmp)
            else:
                cnt = 0



    return answer


print(solution([[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]]))
