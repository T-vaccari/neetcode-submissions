class Solution:

    def encode(self, strs: List[str]) -> str:
        str = ""
        for string in strs :
            str= str+"."+string
        return str

        


    def decode(self, s: str) -> List[str]:
        print(str)
