import sys
sys.stdin = open('input.txt', 'r')

def check():
    for i in range(9):
        sample = []
        for j in range(9):
            if arr[i][j] not in sample:
                sample.append(arr[i][j])
        if len(sample) != 9:
            return False

        sample = []
        for k in range(9):
            if arr[k][i] not in sample:
                sample.append(arr[k][i])
        if len(sample) != 9:
            return False
    return True

def check_2():
    for k in range(0, 9, 3):
        for z in range(0, 9, 3):
            sample = []
            for i in range(k, k + 3):
                for j in range(z, z + 3):
                    if arr[i][j] not in sample:
                        sample.append(arr[i][j])
            if len(sample) != 9:
                return False
    return True

T = int(input())

for t in range(T):
    arr = [list(map(int, input().split())) for _ in range(9)]

    if check() and check_2():
        print('#{} 1'.format(t+1))
    else:
        print('#{} 0'.format(t+1))
