class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # method 1
        merged = nums1[:m] + nums2
        merged.sort()
        for i in range(len(nums1)):
            nums1[i] = merged[i]

        # method 2
        # j = 0
        # for i in range(m,len(nums1)):
        #     nums1[i] = nums2[j]
        #     j+=1 
        # nums1.sort()

        