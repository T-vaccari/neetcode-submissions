class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            res = res + str(len(string)) + "#" + string
        print(res)
        return res
    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            j = i
            while s[j] != "#":
                j = j+1
            lenght = int(s[i:j])
            res.append(s[j+1:j+1+lenght])
            i = j+1+lenght
        return res
            

            

