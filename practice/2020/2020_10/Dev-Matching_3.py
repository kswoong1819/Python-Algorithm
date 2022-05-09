def solution(n, groups):
    global answer
    answer = n
    groups.sort()
    st, ed = groups[0]
    i = 1
    while len(groups) > i:
        st2, ed2 = groups[i]
        if ed2 <= ed:
            groups.pop(i)
        elif st == st2 and ed2 >= ed:
            st, ed = st2, ed2
            groups.pop(i - 1)
        else:
            st, ed = st2, ed2
            i += 1
    used = [0] * len(groups)
    N = [0] * (n + 1)
    N[0] = 1
    tracking(N, groups, used, 0, 0)
    return answer


def tracking(arr, groups, used, cnt, st):
    global answer
    l = len(groups)
    for i in range(st, l):
        if used[i] == 1:
            continue
        used[i] = 1
        n_arr = arr.copy()
        n_arr[groups[i][0]:groups[i][1] + 1] = [1] * (groups[i][1] + 1 - groups[i][0])
        tmp = n_arr.count(0) + cnt + 1
        if tmp < answer:
            answer = n_arr.count(0) + cnt + 1
        tracking(n_arr, groups, used, cnt + 1, i+1)
        used[i] = 0


# n = 100
# groups = [[1, 50], [1, 100], [51, 100]]
# n = 10
# groups = [[1, 5], [2, 7], [4, 8], [3, 6]]
n = 7
groups = [[6, 7], [1, 4], [2, 4]]
print(solution(n, groups))
