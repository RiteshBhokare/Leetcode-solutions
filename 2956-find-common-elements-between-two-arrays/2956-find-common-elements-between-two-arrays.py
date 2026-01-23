class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        cnt1 = 0
        cnt2 = 0
        for i in nums1:
            if i in nums2:
                cnt1 += 1
        for i in nums2:
            if i in nums1:
                cnt2 += 1
        return [cnt1, cnt2]