class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l=[]
        for ele in nums1:
            idx = nums2.index(ele)
            sl = nums2[idx:]
            i=0
            while i < len(sl):
                if idx == len(nums2)-1:
                    l.append(-1)
                    break
                elif nums2[idx] < sl[i]:
                    l.append(sl[i])
                    break
                    
                i+=1
            else:
                l.append(-1)
                    
        return l