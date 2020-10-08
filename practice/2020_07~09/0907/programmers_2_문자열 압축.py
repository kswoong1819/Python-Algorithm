def solution(s):
    answer = float('inf')
    k = 0
    while k < len(s) // 2 + 1:
        k += 1
        result = ''
        check_w = 0
        cnt = 0
        for i in range(0, len(s), k):
            w = s[i: i+k]
            if check_w == w:
                cnt += 1
            else:
                if cnt == 1:
                    result += check_w
                elif cnt != 0:
                    result += str(cnt) + check_w
                check_w = w
                cnt = 1
        if cnt == 1:
            result += check_w
        else:
            result += str(cnt) + check_w
        if answer > len(result):
            answer = len(result)
    return answer


# S = "aabbaccc"
# S = "ababcdcdababcdcd"
# S = "abcabcdede"
# S = "abcabcabcabcdededededede"
# S = "xababcdcdababcdcd"
S = "a"
print(solution(S))