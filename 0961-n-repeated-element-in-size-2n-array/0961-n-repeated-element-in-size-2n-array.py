class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums)//2
        for ele in nums:
            if nums.count(ele) == n:
                return ele
        return -1