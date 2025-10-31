class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        for i in set(ransomNote):
            curr = i
            if ransomNote.count(curr) > magazine.count(curr):
                return False
        return True