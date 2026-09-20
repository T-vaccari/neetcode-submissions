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
        #window = [l, r)
        #occ = exact frequencies inside [l, r)
        #[l, r) is valid
        #r = next character to try to insert
            
        while r < len(s):
            

            # Now I insert the new character into stats, and try to see if the window is ok
            occ[s[r]] = occ.get(s[r], 0) + 1
            top_char = max(occ, key=lambda c: occ[c]) 
            occ_top_char = occ[top_char] 
            subseq_len = r - l + 1
            to_change = subseq_len - occ_top_char

            if to_change <= k:
                #all good go ahead
                r +=1
                max_len = max(max_len, r - l)
            else:
                # I need to move on l until i get a valid state
                # and then increment r

                while True:
                    # Here we are considering 
                    # [l, r]
                    occ[s[l]] -= 1
                    l += 1
                    top_char = max(occ, key=lambda c: occ[c]) 
                    occ_top_char = occ[top_char] 
                    subseq_len = r - l + 1
                    to_change = subseq_len - occ_top_char
                    if to_change <= k:
                        # we are all set
                        r +=1
                        max_len = max(max_len, r - l)
                        break

        return max_len 

                    










            



                










        