import sys
sys.stdin = open('input.txt')

def go(n, start, out):
    if start == 6:
        for i in out:
            print(i, end=' ')
        print()
        return
    if n >= len(nums):
        return
    out.append(nums[n])
    go(n+1, start+1, out)
    out.pop()
    go(n+1, start, out)



while 1:
    nums = list(map(int, input().split()))

    if nums[0] == 0:
        break
    go(1, 0, [])
    print()