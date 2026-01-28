class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        elesum = 0
        for i in nums:
            if i > 9:
                curr = str(i)
                for i in curr:
                    elesum += int(i)
            else:
                elesum += i
        return abs(elesum - sum(nums))