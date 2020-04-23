n = int(input())
arr = [int(input()) for _ in range(n)]
nums = [i for i in range(1,n+1)]
stack, ans = [], []
flag = True

for i in range(n):
    if not flag:
        break
    for k in range(n):
        if arr[i] in stack:
            if arr[i] == stack[-1]:
                stack.pop()
                ans.append('-')
                break
            else:
                flag = False
                break
        else:
            stack.append(nums[0])
            nums.pop(0)
            ans.append('+')

if flag:
    for i in range(len(ans)):
        print(ans[i])
else:
    print('NO')