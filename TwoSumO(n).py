# Importing the List type from the typing module
from typing import List

# Defining the Solution class
class Solution:
    # Defining the twoSum method, which takes a list of integers (nums) and an integer (target) as arguments,
    # and returns a list of integers as the return type
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Creating an empty dictionary to store elements and their indices
        numMap = {}
        # Getting the length of the input list
        n = len(nums)

        # Iterating through the indices of the input list
        for i in range(n):
            # Calculating the complement of the current element with respect to the target
            complement = target - nums[i]
            # Checking if the complement exists in the dictionary (numMap)
            if complement in numMap:
                # If the complement is found, returning a list containing the indices of the two elements that sum up to the target
                return [numMap[complement], i]
            # If the complement is not found, adding the current element to the dictionary along with its index
            numMap[nums[i]] = i

        # If no valid pair is found, returning an empty list
        return []  # No solution found

# Example usage:
if __name__ == "__main__":
    # Create an instance of the Solution class
    solution = Solution()

    # Sample input
    nums = [1, 8, 11, 15]
    target = 9

    # Call the twoSum method on the instance with the sample input
    result = solution.twoSum(nums, target)

    # Print the output
    print("Output:", result)




    # The solution uses a dictionary (numMap) to efficiently 
    # store elements and their indices as it iterates through the array. 
    # The time complexity of this solution is O(n) since it only requires 
    # a single pass through the array.
