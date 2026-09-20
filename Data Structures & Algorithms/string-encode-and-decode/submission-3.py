class Solution:

    def encode(self, strs: List[str]) -> str:
        str = ""
        return ";:".join(strs)

        


    def decode(self, s: str) -> List[str]:
        temp=""
        returnlist = []
        for letter in str:
            if(letter == ";"):
                returnlist.append(temp)
                temp = ""
            
            else:
                temp = temp+letter
        return returnlist

