class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for string in strs :
            output = output +string+  "!0" 
        
        
        print(output)
        return output
    def decode(self, s: str) -> List[str]:
        output = list()
        string = ""
        i = 0
        while i < len(s):
            if s[i] == "!" and s[i+1] == "0":
                output.append(string)
                string = ""
                i  = i+2
            else:
                string = string + s[i]
                i = i+1
        print(output)
        return output
                

            


