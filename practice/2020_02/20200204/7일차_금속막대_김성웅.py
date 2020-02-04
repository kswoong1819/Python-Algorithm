import sys
sys.stdin = open('input.txt', 'r')



T = int(input())

for t in range(T):
    pair = int(input())
    screw = input().split()
    pair_list = []

    for i in range(0, len(screw), 2):
        pair_1 = [screw[i], screw[i+1]]
        pair_list.append(pair_1)
    print(pair_list)


    for x in range(pair):
        pair_list -= pair_list[x]
        print(pair_list)
        # for y in pair_list:
        #     print(y)