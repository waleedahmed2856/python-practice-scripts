nums = [12, 3, 6, 1, 9, 18, 15, 38, 35]

largest = nums[0]
second_largest = nums[0]

for num in nums:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print("Second largest:", second_largest)
