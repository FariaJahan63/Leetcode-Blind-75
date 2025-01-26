def max_product_subarray(nums):
    max_product=nums[0]
    min_product=nums[0]
    result=nums[0]
    for i in range(1,len(nums)):
        num=nums[i]
        if num<0:
            max_product,min_product=max_product,min_product
        max_product=max(num,max_product*num)    
        min_product=min(num,min_product*num)
        result=max(result,max_product)
    return result    
if __name__ == "__main__":
    nums = list(map(int, input("Enter the array elements separated by spaces: ").split()))
    result = max_product_subarray(nums)
    print("Maximum subarray product:", result)