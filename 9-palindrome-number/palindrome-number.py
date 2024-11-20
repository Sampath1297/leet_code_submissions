class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are not palindromes
        if x < 0:
            return False
        
        # Convert the number to a string
        str_x = str(x)
        
        # Check if the string is equal to its reverse
        return str_x == str_x[::-1]

# Example usage
solution = Solution()

x1 = 121
print(solution.isPalindrome(x1))  # Output: True

x2 = -121
print(solution.isPalindrome(x2))  # Output: False

x3 = 10
print(solution.isPalindrome(x3))  # Output: False