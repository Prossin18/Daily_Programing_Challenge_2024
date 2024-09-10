



#arr = [1,2,3,4]

#for i in range(0,len(arr)+1):
  #  if i+1 != arr[i]:
        
        
    
    #    print(i+1)
      #  break
arr = [1, 2, 3, 4]

# Iterate from 1 to len(arr) + 1
for i in range(1, len(arr) + 2):
    if i not in arr:
        print(i)
        break
