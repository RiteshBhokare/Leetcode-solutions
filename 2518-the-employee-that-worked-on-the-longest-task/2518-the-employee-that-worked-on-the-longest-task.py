class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        N=len(logs)
        l=[]
        prev=0
        for ele in logs:
            l.append([ele[1]-prev,ele[0]])
            prev = ele[1]

        l.sort()
        l2=[]
        for i in range(len(l)):
            if l[i][0] == l[N-1][0]:
                l2.append(l[i][1])
        return min(l2)