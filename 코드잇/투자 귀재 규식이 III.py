def sublist_max(profits):
    # 코드를 작성하세요.
    max_profit_so_far = profits[0]
    max_check = profits[0]

    for i in range(1, len(profits)):
        max_check = max(max_check + profits[i], profits[i])
        max_profit_so_far = max(max_profit_so_far, max_check)

    return max_profit_so_far

# 테스트
print(sublist_max([7, -3, 4, -8]))
print(sublist_max([-2, -3, 4, -1, -2, 1, 5, -3, -1]))