class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        s1 = list(set(s))
        cnt = s.count(s1[0])
        for i in range(1,len(s1)):
            if s.count(s1[i]) != cnt:
                return False
        return True
        