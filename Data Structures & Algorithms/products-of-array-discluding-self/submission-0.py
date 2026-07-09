class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #The idea is to avoid to recompute things by exploiting prefix ans suffix.
        # I have two arrays. In the first array, in each cell I maintain the product of all the 
        # elements on the left of the element in that cell, in the other hand in the second
        # array I maintain instead the product.

        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        res = [1] * len(nums)
        i = 1
        while i < len(nums):
            prefix[i] = prefix[i-1] * nums[i-1]
            i+=1
        
        i = len(nums) - 2
        # Instead of having a second array I can directly compute the suffix and store it in the array
        
        while i >= 0:
            
            suffix[i] = suffix[i+1] * nums[i+1]
            i-=1

        for i in range(len(nums)):
            res[i] = prefix[i] * suffix[i]

        # T(n) = O (N)
        # S(n) = O(N)
        return res

        