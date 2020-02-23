nums = map(int, input().split())

cnt_odd = 0
cnt_even = 0
for i in nums:
    if i % 2:
       cnt_odd += 1
    else:
        cnt_even += 1

print('even : {}'.format(cnt_even))
print('odd : {}'.format(cnt_odd))