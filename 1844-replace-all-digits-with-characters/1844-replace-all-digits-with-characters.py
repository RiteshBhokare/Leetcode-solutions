class Solution:
    def replaceDigits(self, s: str) -> str:
        s1 = ""
        for i in range(len(s)):
            if s[i].isdigit():
                curr = ord(s[i-1])+int(s[i])
                s1 += chr(curr)
            else:
                s1+= s[i]
        return s1