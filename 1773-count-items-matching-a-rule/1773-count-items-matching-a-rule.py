class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        cnt = 0
        for ele in items:
            if (ruleKey == "type") &  (ele[0] == ruleValue):
                cnt+=1
            elif (ruleKey == "color") &  (ele[1] == ruleValue):
                cnt+=1
            elif (ruleKey == "name") &  (ele[2] == ruleValue):
                cnt+=1
        return cnt