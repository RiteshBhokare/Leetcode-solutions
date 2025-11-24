class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        curr = ""
        for i in range(len(nums)):
            curr += str(nums[i])
            nums[i] = int(curr,2)%5 == 0
        return nums