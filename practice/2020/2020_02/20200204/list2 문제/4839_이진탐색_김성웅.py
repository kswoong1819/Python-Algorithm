import sys
sys.stdin = open('input.txt', 'r')

def find_num_count(p,n):
    l = 1
    r = p
    c = int((l + r) / 2)
    count = 0
    while n != c:
        count += 1
        c = int((l + r) / 2)
        if n < c:
            r = c
        elif n > c:
            l = c
        else:
            return count
    return count

T = int(input())

for t in range(T):
    P, A, B = map(int, input().split())
    count_A = find_num_count(P,A)
    count_B = find_num_count(P,B)
    if count_A < count_B:
        print('#{} A'.format(t + 1))
    elif count_A == count_B:
        print('#{} 0'.format(t + 1))
    else:
        print('#{} B'.format(t + 1))