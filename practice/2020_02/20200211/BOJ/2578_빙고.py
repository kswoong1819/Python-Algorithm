import sys
sys.stdin = open('input.txt', 'r')

def bingo_check():
    cnt = 0
    d_list = []
    d2_list = []
    for i in range(5):
        j_list = []
        d_list.append(bingo[i][i])
        d2_list.append(bingo[i][4-i])
        if bingo[i] == [0]*5:
            cnt += 1
        for j in range(5):
            j_list.append(bingo[j][i])
            if j_list == [0]*5:
                cnt += 1
    if d_list == [0]*5:
        cnt += 1
    if d2_list == [0]*5:
        cnt += 1
    return cnt

def re():
    for x in number:
        for i in range(5):
            for j in range(5):
                if bingo[i][j] == x:
                    bingo[i][j] = 0
                if bingo_check() >= 3:
                    return x


bingo = [list(map(int, input().split())) for _ in range(5)]
number_tmp = [list(map(int, input().split())) for _ in range(5)]

number = []
for i in range(5):
    for j in range(5):
        number.append(number_tmp[i][j])

print(number.index(re())+1)


