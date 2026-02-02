class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0: return True
        if len(s) > len(t) : return False
        cnt = 0
        for i in range(len(t)):
            if cnt <= len(s)-1:
                if s[cnt] == t[i]:
                    cnt += 1
        return cnt == len(s)
         