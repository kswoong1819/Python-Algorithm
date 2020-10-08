def solution(histogram):
    answer = 0
    L = len(histogram)
    a = 0
    for i in range(L - 2):
        for j in range(i + 2, L):
            low = min(histogram[i], histogram[j])
            tmp = (j - i - 1) * low
            if answer < tmp:
                answer = tmp
    return answer


histogram = [6, 5, 7, 3, 4, 2]
print(solution(histogram))
