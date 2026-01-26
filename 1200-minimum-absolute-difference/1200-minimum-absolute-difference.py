class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        # diff = abs(arr[0]-arr[1])
        # ans = [[arr[0], arr[1]]]
        # print(arr)
        diff = float("inf")
        for i in range(len(arr)-1):
            curr = abs(arr[i] - arr[i+1])
            if diff > curr:
                diff = curr
                idx1 = i
                idx2 = i+1
        ans = {arr[idx1]: arr[idx2]}
        for i in range(1,len(arr)-1):
            if abs(arr[i]-arr[i+1]) == diff:
                ans[arr[i]] = arr[i+1]
        return list(ans.items())
        # print(ans)