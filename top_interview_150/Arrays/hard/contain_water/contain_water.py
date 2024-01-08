class Solution:
    def trap(self, height: List[int]) -> int:
        water_level = [0 for _ in range(len(height))]

        left_wall = None
        for i in range(len(height)):
            if left_wall is None or left_wall <= height[i]:
                left_wall = height[i]
            else:
                water_level[i] = left_wall

        right_wall = None
        for i in reversed(range(len(height))):
            if right_wall is None or height[i] >= right_wall:
                water_level[i] = 0
                right_wall = height[i]
            elif water_level[i] == 0:
                pass
            else:
                water_level[i] = (min(water_level[i], right_wall)) - height[i]
        return sum(water_level)