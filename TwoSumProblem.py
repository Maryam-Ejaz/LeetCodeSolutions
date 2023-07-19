# TWO SUM PROBLEM
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.


class Solution:
    def twoSum(self, nums, target):
        # Get the length of the input list
        n = len(nums)
        
        # Iterate over the elements of the list
        for i in range(n - 1):
            for j in range(i + 1, n):
                # Check if the sum of two elements at indices i and j is equal to the target
                if nums[i] + nums[j] == target:
                    # If a pair is found, return their indices as a list
                    return [i, j]
        
        # If no valid pair is found, return an empty list
        return []
    
# Example usage:
nums = [1, 7, 8, 15]
target = 9

# Create an instance of the Solution class
solution = Solution()

# Call the twoSum method on the instance, passing the nums and target arguments
result = solution.twoSum(nums, target)
print(result)
