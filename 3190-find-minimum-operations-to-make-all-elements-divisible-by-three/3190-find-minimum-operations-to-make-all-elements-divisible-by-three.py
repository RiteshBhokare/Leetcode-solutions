class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = 0
        for i in nums:
            if i%3 != 0:
                count += min(i%3, 3-(i%3))
        return count