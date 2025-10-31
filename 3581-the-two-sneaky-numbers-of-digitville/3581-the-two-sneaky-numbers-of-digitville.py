class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        l = set()
        for ele in nums:
            if nums.count(ele) == 2:
                l.add(ele)
            if len(nums) == 2:
                return list(l)
        return list(l)