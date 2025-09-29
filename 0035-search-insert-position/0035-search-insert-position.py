class Solution(object):
    def searchInsert(self, nums, target):

        prev = None
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            elif nums[i]>target>prev:
                return i
            prev = nums[i]
        else:
            return len(nums)

        