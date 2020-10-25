def solution(n):
    answer = 0
    tmp = ''
    while n:
        a = n % 3
        tmp += str(a)
        n //= 3
    for i in range(len(tmp)):
        answer += int(tmp[(-1 - i)]) * 3 ** i
    return answer


n = 125
print(solution(n))
