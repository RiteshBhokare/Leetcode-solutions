class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        cf = 0
        
        for i in range(1,max(a,b)+1):
            if (a % i == 0) & (b % i == 0):
                cf +=1
        return cf