class Solution:
    def interpret(self, command: str) -> str:
        res = ""
        i = 0
        prev = ""
        while i < len(command):
            if (command[i] == ")") | (command[i] == "("):
                if prev == "(":
                    res += "o"
                    
                
                prev = command[i]
                i += 1
            else:
                prev = ""
                res += command[i]
                i+=1
        return res    

