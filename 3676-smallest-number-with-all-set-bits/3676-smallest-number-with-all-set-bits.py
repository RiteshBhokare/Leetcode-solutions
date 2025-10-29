class Solution:
    def smallestNumber(self, n: int) -> int:
        binary = bin(n)
        binary = binary[2:]
        s=""  
        for ele in binary:
            s += "1"
        return int(s,2)