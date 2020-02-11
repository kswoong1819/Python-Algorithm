import sys
sys.stdin = open('input.txt', 'r')

def find_max(ch_list):
    max_num = 0
    for i in range(len(ch_list) - 1):
        tmp = ch_list[i + 1] - ch_list[i]
        if max_num < tmp:
            max_num = tmp
    return max_num

ga, se = map(int, input().split())
line_count = int(input())

se_list = [0, se]
ga_list = [0, ga]
for i in range(line_count):
    dir, num = map(int, input().split())

    if dir == 1:
        ga_list.append(num)
    if dir == 0:
        se_list.append(num)

se_list.sort()
ga_list.sort()

print(find_max(se_list) * find_max(ga_list))