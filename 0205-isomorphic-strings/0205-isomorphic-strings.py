class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d1 = {}
        d2 = {}

        # if len(s) != len(t):
        #     return False
        
        # for i in range(len(s)):
        #     if (s[i] not in d) & (t[i] not in d.values()):
        #         d[s[i]] = t[i]
        #     if d.get(s[i]) != t[i]:
        #         return False
        # return True

        for k,v in zip(s,t):
            if (k not in d1) & (v not in d2):
                d1[k] = v
                d2[v] = k
            else:
                if (k in d1):
                    if (d1[k] != v):
                        return False
                else:
                    if d2[v] != k:
                        return False
        return True
