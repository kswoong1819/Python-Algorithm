def solution(numbers):
    answer = []
    nums = numbers
    L = len(nums)
    for i in range(L - 1):
        for j in range(i + 1, L):
            tmp = nums[i] + nums[j]
            if tmp not in answer:
                answer.append(tmp)
    answer.sort()
    return answer


# n = [2, 1, 3, 4, 1]
# n = [5, 0, 2, 7]
n = [0, 0]
print(solution(n))
