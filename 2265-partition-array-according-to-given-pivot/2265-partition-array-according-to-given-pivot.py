class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []
        greater = []
        for i in nums:
            if i>pivot:
                greater.append(i)
            elif i<pivot:
                less.append(i)
            else:
                greater.insert(0,i)
        return less+greater