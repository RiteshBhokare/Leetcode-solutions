class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        prefix = [inf] * k
        prefix[-1] = 0
        res = -inf
        for i, pre in enumerate(accumulate(nums)):
            res = max(res, pre - prefix[i%k])
            prefix[i%k] = min(prefix[i%k], pre)
        return res