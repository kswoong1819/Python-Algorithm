import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
calcul = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

for t in range(T):
    mon1, day1, mon2, day2 = map(int, input().split())

    if mon1 == mon2:
        days = day2 - day1 + 1
    else:
        days = 0
        for i in range(mon1, mon2):
            days += calcul[i]
        days = days - day1 + day2 +1

    print('#{} {}'. format(t+1, days))