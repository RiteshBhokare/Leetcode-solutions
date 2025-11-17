class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        dist = 0
        flag = False
        for ele in nums:
            if ele == 1:
                if (dist <= k) and (flag):
                    return False
                flag=True
                dist = 0
            dist+=1
        return True

            