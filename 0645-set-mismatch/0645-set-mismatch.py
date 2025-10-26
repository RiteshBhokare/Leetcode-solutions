class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        dup = nums[0]
        
        
        for i in range(1,len(nums)):
            if nums[i-1] == nums[i]:
                dup = nums[i]
                break

        for i in range(1,len(nums)+1):   
            if i not in nums:
                return [dup,i]
            
            

