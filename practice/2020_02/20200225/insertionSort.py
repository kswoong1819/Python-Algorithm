def insertionSort(n):
    for size in range(1, len(n)):
        val = n[size]
        i = size
        while i > 0 and n[i - 1] > val:
            n[i] = n[i-1]
            i -= 1
        n[i] = val

A = [5,4,3,2,1]
insertionSort(A)
print(A)