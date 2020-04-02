def solution(numbers, target):
    answer = 0

    n = len(numbers)
    for i in range(1<<n):
        for j in range(n):
            if i & (1 << j):
                tmp += arr[j]


    return answer

print(solution([1, 1, 1, 1, 1], 3))