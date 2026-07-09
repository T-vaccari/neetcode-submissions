from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # The idea is to explore the array with two pointers, the left pointer 
        # and the right pointer. The left one signals the start of the probable sequence and the right
        # one is the one that explores. 
        # When the sequence breaks, we can restart from the break point given that no sequence can be longer
        # then the one that we have seen.

        # Oss: they do not have to be consecutive
        if nums is None:
            return 0

        nums = set(nums)
        longest = 0
        for num in nums:
            if num-1 not in nums:
                # it's the start of a sequence
                current = num
                length = 0
                while current in nums:
                    length +=1
                    current+=1
                
                longest = max (longest, length)

        

        return longest




