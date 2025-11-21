class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        cnt = 0
        for ele in words:
            for e in ele:
                if e not in allowed:
                    break
            else:
                cnt+=1
        return cnt