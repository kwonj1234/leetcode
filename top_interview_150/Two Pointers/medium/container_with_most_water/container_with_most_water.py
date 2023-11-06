class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        current_max = 0

        while j > i:
            h = height[i] if height[i] <= height[j] else height[j]
            area = h * (j - i)

            if area > current_max:
                current_max = area

            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
                
        return current_max