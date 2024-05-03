def find_missing_number(nums):
    n = len(nums) + 1
    total = n * (n + 1) // 2
    return total - sum(nums)

numbers = [1, 2, 3, 5, 6, 7, 8]
missing_number = find_missing_number(numbers)
print("The missing number is:", missing_number)
