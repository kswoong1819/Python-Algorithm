import sys
sys.stdin = open('../list_2/input.txt', 'r')

for t in range(10):
    dump = int(input())
    box = list(map(int, input().split()))

    for i in range(dump):
        box.sort()
        box[-1] -= 1
        box[0] += 1

    box.sort()
    print('#{} {}'.format(t+1, box[-1] - box[0]))