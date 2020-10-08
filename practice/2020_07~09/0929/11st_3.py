def solution(A):
    A.sort()
    result = 0
    cnt = 1
    for a in A:
        result += abs(a - cnt)
        cnt += 1
    return result


A = [5, 5, 5, 5, 5]
print(solution(A))
