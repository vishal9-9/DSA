# Stable Sorting

# WORKS like compare 6 with 4 as 4 is small swaps them [4, 6 .....
# Then Compare 1 with 4 and then swaps them as 1 is small then continues to compare 1 with 6 and again swaps [1, 4, 6....

list1 = [6, 4, 1, 3, 9, 10, 10]

for i in range(1, len(list1)):
    j = i - 1
    while j >= 0 and list1[j] > list1[j + 1]:
        temp = list1[j]
        list1[j] = list1[j + 1]
        list1[j + 1] = temp
        j -= 1

print(list1)
