class Solution:
    def reverseWords(self, s: str) -> str:
        li = s.split()
        for i in range(len(li)):
            curr = li[i]
            li[i] = curr[::-1]
        return " ".join(li)