class Solution:

    def encode(self, strs: List[str]) -> str:
        str = ""
        return "#".join(strs)

        


    def decode(self, s: str) -> List[str]:
        print(s)
        temp=""
        returnlist = []
        for letter in s:
            if(letter == "#"):
                returnlist.append(temp)
                temp = ""
            
            else:
                temp = temp+letter
        return returnlist

