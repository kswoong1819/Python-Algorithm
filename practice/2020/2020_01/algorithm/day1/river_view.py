import sys;
sys.stdin = open('input.txt','r')

def bubblesort(a):
    for i in range(len(a)-1,0,-1):
        for j in range(0,i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
def find_max(a):
    findmax = a[0]
    for i in range(1, len(a)):
        if findmax < a[i]:
            findmax = a[i]
    return findmax


for t in range(10):
    list_5 = []
    result = 0
    test_count = int(input())
    arr = list(map(int, input().split()))
    for i in range(2, len(arr)-2):
        for j in range(i-2,i+3):
            list_5.append(arr[j])

        if list_5[2] == find_max(list_5):
            bubblesort(list_5)
            count = list_5[4] - list_5[3]
            result += count
        list_5.clear()
    print('#{} {}'.format(t+1,result))