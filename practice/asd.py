def go(k, cur):
    if k == 3:
        print(cur)
        return
    go(k + 1, cur + A[k])
    go(k + 1, cur)


A = [1,10,100]
go(0,0)