class Solution:

    def encode(self, strs: List[str]) -> str:
        
        res = ""
        #Formattation : lengthString#lengthString#
        for s in strs:
            res = res + str(len(s)) + "#" +  s 

        print(res)
        return res




    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            num = ""
            while s[i] != "#":
                num = num + s[i]
                i = i+1
            
            # Ora converto la stringa numero in numero
            length = int(num)
        
            i+=1 #skip #
           
            res.append(s[i:i+length])
            i+= length
        return res


            



    #Analysis
    # Encode
    # Where n is the number of string and m is the average length
    # Time Complexity : O(N)
    # Space complexity: O(N*M)

    # Decode
    # Time O(N)
    # Space O(M)

