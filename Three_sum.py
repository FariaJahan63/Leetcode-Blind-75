"""class solution:
    def three_sum(self,nums):
        nums.sort()
        result=[]
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l,r=i+1,len(nums)-1 #defining j and k pointer
            while l<r:
                answer=nums[i]+nums[l]+nums[r]
                if answer==0:
                    result.append([nums[i],nums[l],nums[r]])
                    #ignoring duplicates for  2nd &3rd numbers
                    while l<r and nums [l]==nums[l+1]:
                        l+=1
                    while l<r and nums [r]==nums[r-1]:
                        r-=1    
                    l+=1
                    r-=1
                elif answer<0:
                    l+=1
                else:
                    r-=1
        return result                   
if __name__ == "__main__":
    nums = list(map(int, input("Enter the array elements separated by spaces: ").split()))
    
    result=three_sum(nums)
    print("three sum", result)"""
    
def three_sum(nums):
    nums.sort()  # Step 1: Sort the array
    result = []

    for i in range(len(nums) - 2):
        # Skip duplicate values for the first number
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        j,k = i + 1, len(nums) - 1  # Two pointers

        while j<k:
            total = nums[i] + nums[j] + nums[k]

            if total == 0:
                result.append([nums[i], nums[j], nums[k]])

                # Skip duplicate values for the second and third numbers
                while j < k and nums[j] == nums[j + 1]:
                    j += 1
                while j < k and nums[k] == nums[k - 1]:
                    k -= 1

                j += 1
                k -= 1

            elif total < 0:
                j += 1  # Move j pointer to increase sum
            else:
                k -= 1  # Move k pointer to decrease sum

    return result

# Input and running the function
if __name__ == "__main__":
    nums = list(map(int, input("Enter the array elements separated by spaces: ").split()))
    print("Triplets that sum to zero:", three_sum(nums))
    