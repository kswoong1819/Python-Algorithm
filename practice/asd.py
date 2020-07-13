from collections import deque

q = deque([[1, 100], [2, 3], [3, 4], [4, 5]])
a = sorted(q, key = lambda x: x[1])
a.reverse()
print(a)
