class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Understand:
        # Input: Integer Array []
        # Output: Integer Array []
        # WID: Finds two integers in the same array that equate to the target.
                    
        # Plan:
        # Iterate through the nums array
        # Create a nested loop and iterate one after it.
        # Compare the current value i and the nested loop value j to seee
        # if it equals the target
        # If it does we output both [i, j]
        # if not we continue ntil the loop is over and output []

        # Implement:

        sums = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    sums.append(i)
                    sums.append(j)
                    return sums
