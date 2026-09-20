class Solution:

    def encode(self, strs: List[str]) -> str:
        stringr = ""
        for string in strs :
            lunghezza = len(string)
            stringr = stringr+ str(lunghezza)+"#"+string
            
        return stringr


        


    def decode(self, s: str) -> List[str]:
        lista = []

        i = 0

        while (i<len(s)):
            j = i
            while (s[j]!= "#"):
                j+=1
            length =int( s[i:j])
            temp = ""
            for k in range (i,j):
                temp+=s[k]
            lista.append(temp)
        return lista

        
        

