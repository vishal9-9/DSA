# Sorted Array
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

l, r = 0, len(arr) - 1

target = 1

found = False

while l <= r:
    mid = (l + r) // 2

    if target > arr[mid]:
        l = mid + 1
    elif target < arr[mid]:
        r = mid - 1
    else:
        found = True
        print(mid)
        break

if not found:
    print("Not Found")
