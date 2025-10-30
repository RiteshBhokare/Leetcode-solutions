class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2=""
        for ele in s:
            if ele.isalnum():
                s2+=ele.lower()
        print(s2)
        s3 = s2[::-1]
        return s2 == s3