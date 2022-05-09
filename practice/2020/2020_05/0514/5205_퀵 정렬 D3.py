import sys

sys.stdin = open('input.txt')


# def quickSort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2]
#     smaller, equal, bigger = [], [], []
#     for num in arr:
#         if num < pivot:
#             smaller.append(num)
#         elif num > pivot:
#             bigger.append(num)
#         else:
#             equal.append(num)
#     return quickSort(smaller) + equal + quickSort(bigger)
#
#
# T = int(input())
# for t in range(T):
#     N = int(input())
#     nums = list(map(int, input().split()))
#
#     result = quickSort(nums)
#
#     print('#{} {}'.format(t + 1, result[N // 2]))

def quick_sort(A, l, r):
    if l < r:
        p = partition(A, l, r)
        quick_sort(A, l, p - 1)
        quick_sort(A, p + 1, r)

def partition(A, l, r):
    pivot = (l + r) // 2
    while l < r :
        while(A[l] < A[pivot] and l < r):
            l += 1
        while(A[r] >= A[pivot] and l < r):
            r -= 1
        if l < r:
            if l == pivot:
                pivot = r
            A[l], A[r] = A[r], A[l]
    A[pivot], A[r] = A[r], A[pivot]
    return r

T = int(input())
for test_case in range(1, 1 + T):
    N = int(input())
    A = list(map(int, input().split()))
    quick_sort(A, 0, N - 1)
    print('#{} {}'.format(test_case, A[N//2]))
