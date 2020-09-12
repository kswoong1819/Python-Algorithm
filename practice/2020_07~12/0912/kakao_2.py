def solution(orders, course):
    global answer
    answer = {}
    for i in range(len(orders) - 1):
        for j in range(i + 1, len(orders)):
            check = {}
            for a in orders[i]:
                check[a] = 1
            for b in orders[j]:
                if b in check:
                    check[b] += 1
            tmp = ''
            for d in check:
                if check[d] == 2:
                    tmp += d
            for c in course:
                if len(tmp) >= c:
                    backtrack(c, tmp, '', 0)

    result = []
    for c in course:
        tmp = []
        max_len = 0
        for w in answer:
            if len(w) == c:
                if max_len < answer[w]:
                    max_len = answer[w]
                    tmp = [w]
                elif max_len == answer[w]:
                    tmp.append(w)
        result.extend(tmp)
    result.sort()
    return result


def backtrack(n, arr, st, k):
    if len(st) == n:
        st = ''.join(sorted(st))
        if st in answer:
            answer[st] += 1
        else:
            answer[st] = 1
        return
    for i in range(k, len(arr)):
        if arr[i] in st:
            continue
        backtrack(n, arr, st + arr[i], i + 1)


# orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
# course = [2, 3, 4]
# orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
# course = [2, 3, 5]
orders = ["XYZ", "XWY", "WXA"]
course = [2, 3, 4]

print(solution(orders, course))
