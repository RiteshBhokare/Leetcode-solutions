class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        mini = 0
        cnt = 0
        if (num1 == 0) | (num2 == 0):
            return 0
        if num1 == num2:
            return 1
        
        while True:
            if num1 >= num2:
                num1 -= num2
            else:
                num2 -= num1
            cnt +=1
            if (num1 == 0) | (num2 == 0):
                return cnt