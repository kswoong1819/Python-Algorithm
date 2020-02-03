import sys
sys.stdin = open('input.txt', 'r')

def max_num(n):
    num = n[0]
    for i in range(len(n)):
        if num < n[i]:
            num = n[i]
    return num

T = int(input())

for t in range(T):
    case = input()
    score_list = list(map(int, input().split()))

    count_list = []
    for score in score_list:
        count = 0
        for i in range(len(score_list)):
            if score == score_list[i]:
                count += 1
        count_list.append(count)
    new_score = []
    for j in range(len(count_list)):
        if count_list[j] == max_num(count_list):
            new_score.append(score_list[j])
    print('#{} {}'.format(t+1, max_num(new_score)))