for tc in range(1,int(input())+1):
    n = int(input())
    rooms = [list(map(int,input().split())) for _ in range(n)]
    ls = [0]*(401)
    for i in range(n):
        for j in range(rooms[i][0],rooms[i][1]+1):
            ls[j] += 1
    print("#{} {}".format(tc,max(ls))))