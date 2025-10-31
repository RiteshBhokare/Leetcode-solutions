class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        for i in range(len(ransomNote)):
            curr = ransomNote[i]
            if ransomNote.count(curr) > magazine.count(curr):
                return False
        return True