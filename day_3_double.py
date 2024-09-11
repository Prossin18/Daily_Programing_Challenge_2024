def extra(arr):
    n = -1
    for i in range(0,len(arr)):
        n=n+i
        if arr[i] == arr[n]:
            
            print(arr[i])
            break


#Test case 1
array1 = [1,4,4,3,2]
extra(array1)

#Test case 2
array2 = [1,3,4,2,2]

#Test case 3
array3 = [1,1]


