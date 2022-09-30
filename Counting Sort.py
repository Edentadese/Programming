def countingSort(arr):
    count = [0] * (max(arr) + 1)
    for i in range(len(arr)):
        count[arr[i]] += 1
    sortedArray=[]
    for i in range(len(count)):
        for j in range(count[i]):
            if count[i] != 0:
                sortedArray.append(i)
    print(*count)
    print(*sortedArray)
countingSort([1,1,1,3,2,1])
