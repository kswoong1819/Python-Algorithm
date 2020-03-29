def solution(stones, k):
    answer = 0
    cnt = 0
    while xnt ==
        for i in range(len(stones)):
            stones[i] -= 1
            if stones[i] < 0:
                cnt += 1
                if cnt == k:
                    break
            else:
                cnt = 0
        answer += 1

    return answer


print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))