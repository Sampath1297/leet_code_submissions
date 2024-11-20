class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        prefix = strs[0]  # Start with the first string as initial prefix
        
        for i in range(1, len(strs)):  # Compare with all other strings
            while strs[i].find(prefix) != 0:  # Check if prefix is at the beginning of strs[i]
                prefix = prefix[:-1]  # If not, remove the last character from prefix
        
        return prefix