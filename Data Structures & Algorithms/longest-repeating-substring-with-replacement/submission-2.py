class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        if not s:
            return 0
        
        if len(s) == 1:
            return 1

        # Given a substring I have to choose as target unique the most frequent character
        # and substitue all the ones that are not that character. 
        # How to choose the rolling window? in the rolling window i need to have
        # at most k characters that differs from the chosen one.

        l = 0
        r = 1

        max_len = 0
        
        occ = dict()

        for r in range(len(s)):
            occ[s[r]] = occ.get(s[r],0) + 1 #Insert he new char

            #Is the current window valid? If not work to make it valid

            while (r - l + 1) - max(occ.values()) > k:
                occ[s[l]] -=1
                l+=1
            
            max_len = max(max_len, r - l + 1)
        
        return max_len

                    










            



                










        