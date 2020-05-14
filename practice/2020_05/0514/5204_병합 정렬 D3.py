def mergeSort(li):
    if len(li) <= 1:
        return li
    mid = len(li) // 2
    left = mergeSort(li[:mid])
    right = mergeSort(li[mid:])
    return merge(left, right)


def merge(left, right):
    global cnt

    left_N, right_N = len(left), len(right)
    result = [0] * (left_N + right_N)
    left_i, right_i = 0, 0
    i = 0

    if left[-1] > right[-1]:
        cnt += 1

    while left_i != left_N and right_i != right_N:
        if left[left_i] <= right[right_i]:
            result[i] += left[left_i]
            i += 1
            left_i += 1
        else:
            result[i] += right[right_i]
            i += 1
            right_i += 1

    if left_i != left_N:
        while left_i != left_N:
            result[i] += left[left_i]
            i += 1
            left_i += 1

    if right_i != right_N:
        while right_i != right_N:
            result[i] += right[right_i]
            i += 1
            right_i += 1

    return result


# def merge(le, ri):
#     global cnt
#     result = []
#     if le[-1] > ri[-1]:
#         cnt += 1
#     while len(le) > 0 and len(ri) > 0:
#         if le[0] <= ri[0]:
#             result.append(le.pop(0))
#         else:
#             result.append(ri.pop(0))
#     if len(le) > 0:
#         result.extend(le)
#     if len(ri) > 0:
#         result.extend(ri)
#     return result


T = int(input())

for t in range(T):
    N = int(input())
    nums = list(map(int, input().split()))
    cnt = 0
    result = mergeSort(nums)

    print('#{} {} {}'.format(t + 1, result[N // 2], cnt))
