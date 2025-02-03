class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        new_digits_list=''.join(map(str,digits))
        integer_value=int(new_digits_list)
        integer_value=integer_value+1
        final_list=list(map(int,str(integer_value)))
        
        return final_list





        