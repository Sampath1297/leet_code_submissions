from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Edge case: If the array is empty, return 0
        if not nums:
            return 0
        
        # Pointer for the position of unique elements
        i = 0
        
        # Traverse the array from the second element
        for j in range(1, len(nums)):
            # When we encounter a new unique element
            if nums[j] != nums[i]:
                i += 1  # Move the pointer for the next unique element
                nums[i] = nums[j]  # Update the array with the unique element
        
        # Return the number of unique elements (i + 1)
        return i + 1


