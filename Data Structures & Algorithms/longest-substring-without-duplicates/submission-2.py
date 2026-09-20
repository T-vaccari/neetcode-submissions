class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if not s or len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        

        l = 0
        r = 1
        chr_seen_in_the_substring = set()
        max_len = 0
        chr_seen_in_the_substring.add(s[l])
        # r is the character we want to introduce, is still non part
        # of the sequence
        while r < len(s):
            max_len = max(max_len, r - l)

            if s[r] in chr_seen_in_the_substring:
                # I try to save as much as possible from the current substring
                while s[r] in chr_seen_in_the_substring:

                    if r == l:
                        r = l + 1
                        break
                    else:
                        chr_seen_in_the_substring.remove(s[l])
                        l +=1
                    
            else:
                # I can add it to the set
                chr_seen_in_the_substring.add(s[r])
                r+=1

        return max_len







        