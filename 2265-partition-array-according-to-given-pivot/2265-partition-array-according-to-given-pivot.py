class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []
        greater = []
        piviotFreq=0
        for i in nums:
            if i>pivot:
                greater.append(i)
            elif i<pivot:
                less.append(i)
            else:
                piviotFreq += 1
        return less + [pivot] * piviotFreq + greater