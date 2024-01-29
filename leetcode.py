import copy


# Two Sum II - Input Array Is Sorted

numbers = [2, 7, 11, 15]
target = 9

l, r = 0, len(numbers) - 1


while l < r:
    sum = numbers[l] + numbers[r]
    if sum < target:
        l += 1
    elif sum > target:
        r -= 1
    elif sum == target:
        print([l + 1, r + 1])
        break

# 3Sum

nums = [-1, 0, 1, 2, -1, -4]

nums.sort()

to_return = []

for i in range(0, len(nums)):
    if i != 0 and nums[i] == nums[i - 1]:
        continue

    l, r = i + 1, len(nums) - 1

    while l < r:
        sum = nums[i] + nums[l] + nums[r]

        if sum < 0:
            l += 1
        elif sum > 0:
            r -= 1
        else:
            to_return.append([nums[i], nums[l], nums[r]])
            l += 1
            while nums[l] == nums[l - 1] and l < r:
                l += 1

print(to_return)

# Trapping Rain Water

height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

l, r = 0, len(height) - 1

max_l = 0
max_r = 0

min_h = []

while l < r:
    l_min = min(max_l, height[l])
    r_min = min(max_r, height[r])

    min_h.append(min(l_min, r_min))
    l += 1
    r -= 1

# Valid Parentheses
s = "{[]}"

stack = []

close_to_open_mapping = {"}": "{", "]": "[", ")": "("}

for i in s:
    if i in close_to_open_mapping:
        if stack and stack[-1] == close_to_open_mapping.get(i):
            stack.pop()
        else:
            print(False)
    else:
        stack.append(i)
print(True)


# Daily Temperatures

temperatures = [73, 74, 75, 71, 69, 72, 76, 73]

# Brute Force Method
to_return = []

for i in range(0, len(temperatures)):
    for j in range(i, len(temperatures)):
        to_break = False
        if temperatures[j] > temperatures[i]:
            to_return.append(j - i)
            to_break = True
            break
    if not to_break:
        to_return.append(0)

print(to_return)

# Longest Common Prefix

strs = ["dog", "racecar", "car"]


def check_strs():
    _element = ""
    for i in strs[0]:
        _element += i
        for j in range(1, len(strs)):
            if not strs[j].startswith(_element):
                return _element[0 : len(_element) - 1] if _element != "" else ""
    return _element


print(check_strs())
