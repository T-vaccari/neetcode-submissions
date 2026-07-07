class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #I can start from the boundaries of the container, and I can move 
        #up one boundary for iteration
        # Only if I can improve the quantity of water
        #that means I can push further the side with the minimu height in search for improvement
        #I think it's a grady algorithm
        left = 0
        right = len(heights) - 1
        maxwater = 0
        while left < right :
            maxwater = max(maxwater, (right-left) * min(heights[left], heights[right]))
            if heights[left] < heights[right]:
                left+=1
            else:
                right-=1

        return maxwater




        