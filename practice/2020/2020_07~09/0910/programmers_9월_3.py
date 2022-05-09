def solution(a):
    answer = 0
    used = [0] * len(a)
    tracking([], used, a, 0)
    return answer


def tracking(b, used, arr, ch):

    for i in range(len(arr)):
        if used[i]: continue
        b.append(arr[i])
        used[i] = 1
        b.p
        


a = [9, -1, -5]
# a = [-16, 27, 65, -2, 58, -92, -71, -68, -61, -33]
print(solution(a))
