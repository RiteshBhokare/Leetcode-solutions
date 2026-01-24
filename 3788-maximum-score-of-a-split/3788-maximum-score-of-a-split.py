class Solution:
    def maximumScore(self, nums: List[int]) -> int:
        total = sum(nums)
        ans = float("-inf")
        mini = float("inf")
        for i in range(len(nums)-1,0,-1):
            total -= nums[i]
            mini = min(mini, nums[i])
            ans = max(ans, total - mini)
        return ans