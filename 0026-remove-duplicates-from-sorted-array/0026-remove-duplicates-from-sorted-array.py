class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        l = []
        while i<len(nums):
            if nums[i] in l:
                nums.pop(i)
            else:
                l.append(nums[i])
                i+=1
        return  len(nums)
        