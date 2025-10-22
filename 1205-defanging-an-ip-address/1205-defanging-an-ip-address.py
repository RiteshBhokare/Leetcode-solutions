class Solution:
    def defangIPaddr(self, address: str) -> str:
        # address2 = ""
        # for i in address:
        #     if i == ".":
        #         address2 += "[.]"
        #     else:
        #         address2+=i
        # return address2

        return address.replace('.','[.]')