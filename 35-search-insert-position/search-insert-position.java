class Solution {
    public int searchInsert(int[] nums, int target) {
        int len = nums.length;
        int index = 0;

        // No need to sort the array, it's already sorted
        for (int i = 0; i < len; i++) {
            if (nums[i] == target) {
                return i;  // Target found, return the index
            } else if (nums[i] > target) {
                return i;  // Target should be inserted here
            }
        }
        
        // If we reach here, the target is greater than all elements, insert at the end
        return len;
    }
}