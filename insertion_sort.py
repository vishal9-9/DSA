arr = [9, 10, 8, 7, 6, 5, 4, 3, 2, 1, 0]

for i in range(1, len(arr)):
    j = i - 1
    while j >= 0 and arr[j] > arr[j + 1]:
        temp = arr[j + 1]
        arr[j + 1] = arr[j]
        arr[j] = temp
        j -= 1

print(arr)
