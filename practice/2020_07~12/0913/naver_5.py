def solution(cards):
    answer = 0
    dealer = []
    player = []
    flag = True
    for i in range(len(cards)):
        card = cards[i]
        if i <= 3:
            if i == 0 or i == 2:
                if card >= 10:
                    card = 10
                if card == 1:
                    if len(dealer) == 0:
                        dealer.append([1])
                        dealer.append([11])
                    else:
                        dealer.append([dealer[0], 1])
                        dealer.append([dealer[0], 11])
                else:
                    if len(dealer) == 0:
                        dealer.append([card])
                    else:
                        k = 0
                        while len(dealer) > k:
                            dealer[k] = [dealer[k][0], card]
                            k += 1
            elif i == 1 or i == 3:
                if card >= 10:
                    card = 10
                if card == 1:
                    if len(player) == 0:
                        player.append([1])
                        player.append([11])
                    else:
                        player.append([player[0], 1])
                        player.append([player[0], 11])
                else:
                    if len(dealer) == 0:
                        player.append([card])
                    else:
                        k = 0
                        while len(player) > k:
                            player[k] = [player[k][0], card]
                            k += 1
        # if i > 3:
        #     if flag:
        #         for i in range(len(player)):
        #             if player[i] == 1:
        #                 tmp = player.copy()
        #                 tmp.remove(1)
        #                 tmp.append(11)
        #                 if (dealer[0] == 1 or dealer[0] >= 7) and sum(tmp) < 17:
        #                     dealer.append(card)
        #                 elif dealer[0] in [2, 3] and sum(tmp) < 12:
        #                     dealer.append(card)
        #     else:
        #         pass

    print(dealer, player)

    return answer


cards = [12, 7, 11, 6, 2, 12]
# cards = [1, 4, 10, 6, 9, 1, 8, 13]
# cards = [10, 13, 10, 1, 2, 3, 4, 5, 6, 2]
# cards = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
print(solution(cards))
