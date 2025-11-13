class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftSum = []
        rightSum = []
        for i in range(len(nums)):
            curr = nums[0:i]
            leftSum.append(sum(curr))         
            rightSum.append(sum(nums[len(nums):i:-1]))

        for i in range(len(leftSum)):
            nums[i] = abs(leftSum[i] - rightSum[i])
        return nums