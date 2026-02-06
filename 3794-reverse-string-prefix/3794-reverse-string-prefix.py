class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        s1 = s[:k]
        s1 = s1[::-1]
        return s1+s[k:]