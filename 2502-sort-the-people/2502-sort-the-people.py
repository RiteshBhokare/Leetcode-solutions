class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        d={}
        for i in range(len(names)):
            d[heights[i]] = names[i]
        d2 = sorted(d, reverse=True)
        l1=[]
        
        for i in d2:
            l1.append(d.get(i))
        return l1