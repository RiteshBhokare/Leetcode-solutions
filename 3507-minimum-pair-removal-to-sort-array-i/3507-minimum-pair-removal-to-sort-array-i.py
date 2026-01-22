class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        def is_non_dec(nums):
            for i in range(1,len(nums)):
                if nums[i] < nums[i-1]:
                    return False
            return True
        cnt = 0
        while not is_non_dec(nums):
            minn = float("inf")
            idx = 0
            for i in range(len(nums)-1):
                if minn > (nums[i]+ nums[i+1]):
                    minn = nums[i] + nums[i+1]
                    idx = i

            nums[idx] = minn
            nums.pop(idx+1)
            cnt += 1

        return cnt
