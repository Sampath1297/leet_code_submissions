class Solution:
    def addBinary(self, a: str, b: str) -> str:
        num1=int(a,2)
        num2=int(b,2)
        num3=num1+num2
        final_string=bin(num3)
        return final_string[2:]
        