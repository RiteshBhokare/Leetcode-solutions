class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        dup = nums[0]
        curr = 1
        
        for i in range(1,len(nums)):
            if nums[i-1] == nums[i]:
                dup = nums[i]
                break

        for i in range(len(nums)):   
            if curr not in nums:
                return [dup,curr]
            
            curr+=1
            

