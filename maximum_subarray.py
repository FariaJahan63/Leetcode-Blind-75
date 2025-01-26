def max_subarray_sum(nums):
    max_sum = nums[0]  # Initialize max sum with the first element
    update_sum = nums[0]  # Initialize update sum

    for i in range(1, len(nums)):
        update_sum = max(nums[i], update_sum + nums[i])  # Extend or start new subarray
        max_sum = max(max_sum, update_sum)  # Update max sum

    return max_sum

if __name__ == "__main__":
    nums = list(map(int, input("Enter the array elements separated by spaces: ").split()))
    result = max_subarray_sum(nums)
    print("Maximum subarray sum:", result)

    