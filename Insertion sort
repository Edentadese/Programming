def insertioSort(n,arr):
    temporary=arr[n-1]
    for i in range(n-1,0,-1):
        if arr[i-1]>temporary:
            arr[i] = arr[i-1]
            print(*arr)
            if arr[i-1]==arr[0]:
                arr[i-1] = temporary
                print(*arr)
        else:
            arr[i] = temporary
            print(*arr)
            break
insertionSort(5,[2,4,6,8,4])

