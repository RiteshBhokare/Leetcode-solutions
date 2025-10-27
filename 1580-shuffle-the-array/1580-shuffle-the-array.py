class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        # l1 = nums[:n]
        # l2 = nums[n:]
        # l3=[]
        # for i in range(n):
        #     l3.append(l1[i])
        #     l3.append(l2[i])
        # return l3

        idx = n
        l=[]
        for i in range(n):
            l.append(nums[i])
            l.append(nums[n])
            n+=1
        return l