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
        occ[s[l]] = 1
        # Invariant r is the character that i have to insert
        # at the moment occ contains [l, r)
        while r < len(s):
            max_len = max(max_len, r - l)
            # Can i insert r without problems or it creates problem? 
            # stats from [l, r)
            top_char = max(occ, key=lambda c: occ[c])
            occ_top_char = occ[top_char] 
            subseq_len = r - l           
            to_change = subseq_len - occ_top_char

            if s[r] == top_char:
                # I have not to pay the substitution
                # insert it and go ahead
                occ[s[r]] = occ.get(s[r], 0) + 1
                r+=1
                max_len = max(max_len, r - l)
            else:
                occ[s[r]] = occ.get(s[r], 0) + 1
                top_char = max(occ, key=lambda c: occ[c])
                occ_top_char = occ[top_char] 
                subseq_len = r - l + 1          
                to_change = subseq_len - occ_top_char
                if to_change <=k:
                    # all good i can go ahead
                    # and insert it into the stats
                    
                    r +=1
                    max_len = max(max_len, r - l)
                else:
                    # I cannot afford to insert it
                    # I must advance l untile i get a clen state and at the end increment r
                    while True:
                        occ[s[l]]-=1
                        l+=1
                        top_char = max(occ, key=lambda c: occ[c])
                        occ_top_char = occ[top_char] 
                        subseq_len = r - l + 1          
                        to_change = subseq_len - occ_top_char
                        
                        if to_change <=k:

                            r += 1
                            max_len = max(max_len, r - l)
                            break
                        



        
        return max_len


            
                










        