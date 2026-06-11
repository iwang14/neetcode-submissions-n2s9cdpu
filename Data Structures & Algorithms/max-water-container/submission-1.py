class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        width = 0
        max_area = 0

        while left < right:
            width = right - left
            current_area = min(heights[right], heights[left]) * width

            max_area = max(current_area, max_area)

            if heights[left]>heights[right]:
                right -= 1
            else:
                left += 1 
                
        return max_area
            
            





    























