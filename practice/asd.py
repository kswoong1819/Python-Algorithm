def func(nowmonth, totalmoney):
    global minimoney
    if nowmonth > 12:
        if minimoney > totalmoney:
            minimoney = totalmoney
        return

    func(nowmonth + 1, (totalmoney + (money[1] * month[nowmonth])))
    func(nowmonth + 1, (totalmoney + money[2]))
    func(nowmonth + 3, (totalmoney + money[3]))


T = int(input())

for tc in range(1, T + 1):
    money = [0] + list(map(int, input().split()))
    month = [0] + list(map(int, input().split()))

    minimoney = money[4]

    func(1, 0)

    print("#{} {}".format(tc, minimoney))
