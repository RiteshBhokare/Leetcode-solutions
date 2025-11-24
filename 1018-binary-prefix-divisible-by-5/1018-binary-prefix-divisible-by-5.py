class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        curr = ""
        # for i in range(len(nums)):
            # curr += str(nums[i])
            # nums[i] = int(curr,2)%5 == 0
        res = []
        rem = 0
        for ele in nums:
            rem = (rem*2 + ele) % 5
            res.append(rem == 0)
        return res