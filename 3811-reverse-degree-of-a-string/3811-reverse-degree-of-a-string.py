class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0
        for i in range(len(s)):
            curr = (ord('z') - ord(s[i]))+1 
            total += (i+1)*curr
        return total