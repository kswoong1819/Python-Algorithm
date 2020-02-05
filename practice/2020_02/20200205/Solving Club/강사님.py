T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    max_value = -1

    for i in range(len(nums) -1):
        for j in range(i + 1, len(nums)):
            num = nums[i] * nums[j]
            tmp_num = num
            prev = 10
            isOK = True

            while num > 0:
                target = num % 10
                if prev < target:
                    isOK = False
                    break
                num = num // 10
                prev = target

            if isOK:
                if max_value < tmp_num:
                    max_value = tmp_num
    print("#{} {}".format(tc, max_value))