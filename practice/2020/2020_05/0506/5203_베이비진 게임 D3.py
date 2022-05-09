def check(card):
    flag = False
    for i in range(10):
        if card[i] >= 3:
            flag = True
            break
        if card[i] > 0 and i < 8:
            if card[i + 1] > 0 and card[i + 2] > 0:
                flag = True
                break
    return flag


T = int(input())

for t in range(T):
    cards = list(map(int, input().split()))

    player1 = [0] * 10
    player2 = [0] * 10

    ans = 0
    for i in range(12):
        if i % 2 == 0:
            player1[cards[i]] += 1
            if check(player1):
                ans = 1
                break
        elif i % 2:
            player2[cards[i]] += 1
            if check(player2):
                ans = 2
                break

    print('#{} {}'.format(t + 1, ans))
