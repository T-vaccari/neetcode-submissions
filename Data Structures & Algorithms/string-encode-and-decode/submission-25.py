class Solution:

    def encode(self, strs: List[str]) -> str:
        
        res = ""
        separator = "!-!"
        for s in strs:
            res = res + s + separator
        return res




    def decode(self, s: str) -> List[str]:
        separator = "!-!"
        return s.split(separator)[:-1]

