def sequence(k,num):
    if k==m:
        for i in range(m):
            print(ls[i],end=' ')
        print()
    else:
        for i in range(num, n+1):
            if visit[i]:continue
            visit[i]=1
            ls[k]=i
            sequence(k+1,i+1)
            visit[i]=0

n,m=map(int,input().split())
ls=[0]*m
visit=[0]*(n+1)
sequence(0,1)