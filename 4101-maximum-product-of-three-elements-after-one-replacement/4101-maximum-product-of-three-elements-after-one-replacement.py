class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        l1 = nums[n-1] * nums[n-2] * 100000
        l1 = max(l1, nums[0]*nums[n-1]*-100000)
        l1 = max(l1, nums[0]*nums[1]*100000)
        return l1