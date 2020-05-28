import collections


def make_max_price():
    dq = collections.deque()
    dq.append((price_lst, n))
    max_price = 0
    f = False
    if len(price) != len(set(price)):
        f = True

    while dq:
        p, cnt = dq.popleft()
        if f or not cnt % 2:
            tmp = int(''.join(p))
            if tmp > max_price:
                max_price = tmp

        if cnt == 0:

            continue

        for i in range(L):
            for j in range(i + 1, L):
                tmp = p[:]
                tmp[i], tmp[j] = tmp[j], tmp[i]
                if not (''.join(tmp) in price_set):
                    price_set.add(''.join(tmp))
                    dq.append((tmp, cnt - 1))
    return max_price


T = int(input())
for t in range(1, T + 1):
    price, n = input().split()
    price_lst, n = list(price), int(n)
    L = len(price)
    price_set = {price}
    print('#%s %s' % (t, make_max_price()))