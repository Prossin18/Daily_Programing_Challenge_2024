def extra(arr):
    n = -1
    for i in range(0,len(arr)):
        n=n+i
        if arr[i] == arr[n]:
            
            print(arr[i])
            break
array = [1,4,4,3,2]

extra(array)
