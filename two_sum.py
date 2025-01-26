"""
class Solution:
    def twoSum(self, nums: List[int], target: int) ->List[int]:
        prevMap={}
        for i, n in enumerate(nums):
            difference=target-n
            if difference in prevMap:
                return [prevMap[difference],i]
            prevMap[n]=i
        return """
class Solution:
    def two_sum(self, numbers, target):
        number_map = {}  # Creates an empty dictionary to store numbers and their indices
        for i, number in enumerate(numbers):
            difference = target - number  # Calculate the number needed to reach the target
            if difference in number_map:  # If the difference is found in the dictionary
                return [number_map[difference], i]  # Return the indices of the two numbers
            # If not found, store the current number and its index in the dictionary
            number_map[number] = i
        return []  # Return an empty list if no solution is found (shouldn't happen per problem constraints)

# Taking input from the user
if __name__ == "__main__":
    # Taking input as space-separated numbers and converting to list of integers
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    
    # Taking target as an integer
    target = int(input("Enter the target number: "))
    
    # Create an instance of the Solution class
    solution = Solution()
    
    # Call the function and print the result
    result = solution.two_sum(numbers, target)
    
    print("Indices:", result)