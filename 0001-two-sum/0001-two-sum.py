class Solution(object):
    def twoSum(self, nums, target):
        l1=[]
        flag = False
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[i] + nums[j] == target):
                    l1.append(i)
                    l1.append(j)
                    flag = True
                if flag:
                    break
            if flag:
                break
        return l1
                    