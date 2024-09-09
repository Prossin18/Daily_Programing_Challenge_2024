arr = [0,1,2,1,0,2,1,0]
for i in range (0 , len(arr)):
    for j in range (0 , len(arr)-1):
        if arr[j] > arr[j+1]:
            arr[j] , arr[j+1] = arr[j+1] , arr[j]
    
print(arr)