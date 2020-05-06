import sys

sys.stdin = open('input.txt')


def check(card):
    card.sort()
    flag = False
    for i in range(len(card) - 2):
        if card[i] == card[i + 1] == card[i + 2]:
            flag = True
            break
        if card[i] == card[i + 1] - 1 == card[i + 2] - 2:
            flag = True
            break
    return flag


T = int(input())

for t in range(T):
    cards = list(map(int, input().split()))

    player1 = []
    player2 = []

    ans = 0
    for i in range(12):
        if i % 2 == 0:
            player1.append(cards[i])
            if check(player1):
                ans = 1
                break
        elif i % 2:
            player2.append(cards[i])
            if check(player2):
                ans = 2
                break

    print('#{} {}'.format(t + 1, ans))
