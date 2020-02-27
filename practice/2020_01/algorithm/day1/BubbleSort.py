def bubblesort(a):
    for i in range(len(a)-1,0,-1):
        for j in range(0,i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

arr = [55,24,84,65,98,15,35]
print(bubblesort(arr))