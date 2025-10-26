class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        s = set(nums)
        for ele in nums: 
            if nums.count(ele) == 2:
                freq = ele
        for i in range(len(nums)):
            if i+1 not in nums:
                return [freq,i+1] 