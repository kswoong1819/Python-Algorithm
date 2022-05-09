# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    cnt = 0
    tmp = 0
    for i in S:
        if i == 'a':
            tmp += 1
            if tmp > 2:
                return -1
        else:
            cnt += 2 - tmp
            tmp = 0
    if tmp > 2:
        return cnt
    else:
        cnt += 2 - tmp
    return cnt


S = ""
print(solution(S))
