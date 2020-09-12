def solution(a):
    answer = 0
    cnt = [0] * len(a[0])
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j] == 1:
                cnt[j] += 1
    skip = []
    for i in range(len(cnt)):
        if cnt[i] == 0 or cnt[i] == len(a):
            skip.append(i)

    makearr(a, cnt, skip)
    return answer


def makearr(arr, c, s):


a = [[0, 1, 0], [1, 1, 1], [1, 1, 0], [0, 1, 1]]
# a = [[1, 0, 0], [1, 0, 0]]
# a = [[1, 0, 0, 1, 1], [0, 0, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 0, 1]]

print(solution(a))
