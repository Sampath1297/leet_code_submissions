class Solution:
    def romanToInt(self, s: str) -> int:
        # Dictionary to store the values of each Roman numeral character
        roman_to_int = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        
        total = 0
        prev_value = 0  # Track value of previous numeral to determine if subtraction is needed
        
        # Iterate the reversed string from left to right
        for char in reversed(s):
            current_value = roman_to_int[char]
            if current_value >= prev_value:
                total += current_value
            else:
                total -= current_value
            prev_value = current_value
        
        return total