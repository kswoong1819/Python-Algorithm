st, ed = map(int, input().split())
if st > ed:
    st, ed = ed, st

num_li = []
for i in range(st, ed+1):
    if i % 3 == 0 or i % 5 == 0:
        num_li.append(i)

result = sum(num_li)
avg = result/len(num_li)

print('sum : {}'.format(result))
print('avg : {:.1f}'.format(avg))