import sys;
sys.stdin = open('input.txt','r')

for T in range(1,11):
    N = int(input())
    arr = list(map(int, input().split()))

    ans = 0
    for i in range(2, N-2):
        # i번 값이 (i-2, i-1, i+1, i+2) 보다 큰 값
        Max = max(arr[i-2], arr[i-1], arr[i+1], arr[i+2])
        if arr[i] > Max:
            ans += arr[i] - Max

    print('#%d %d' %(T, ans))