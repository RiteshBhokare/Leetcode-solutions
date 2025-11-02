class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        idx = min(nums)
        l = []
        for i in range(min(nums),max(nums)):
            idx+=1
            if idx not in nums:
                l.append(idx)
        return l 