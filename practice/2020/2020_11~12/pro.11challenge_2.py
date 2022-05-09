def solution(s):
    answer = [0, 0]
    while s != '1':
        answer[1] += str(s).count('0')
        s = format(str(s).count('1'), 'b')
        answer[0] += 1
    return answer


s = 110010101001
print(solution(s))
