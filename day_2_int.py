
arr = [1, 2, 3, 4]

# Iterate from 1 to len(arr) + 1
for i in range(1, len(arr) + 2):
    if i not in arr:
        print(i)
        break
