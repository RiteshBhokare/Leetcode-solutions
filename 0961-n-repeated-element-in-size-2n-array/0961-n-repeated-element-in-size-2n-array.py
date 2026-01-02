class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        l = []
        for ele in nums:
            if ele in l:
                return ele
            l.append(ele)