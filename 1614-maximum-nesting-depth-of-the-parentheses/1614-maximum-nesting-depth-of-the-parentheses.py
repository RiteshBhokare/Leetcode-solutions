class Solution:
    def maxDepth(self, s: str) -> int:
        maxp = 0
        m=0
        for ele in s:
            if ele == "(":
                maxp += 1
                if m < maxp:
                    m = maxp
            elif ele == ")":
                maxp -= 1 
        return m