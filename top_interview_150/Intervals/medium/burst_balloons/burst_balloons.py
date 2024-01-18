class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        ans = 0
        overlap = None
        points.sort(key=lambda x: x[0])
        
        for point in points:
            if overlap is None:
                overlap = point
                ans += 1
            elif overlap[0] <= point[0] <= overlap[1]:
                overlap[0] = point[0]
                overlap[1] = point[1] if overlap[1] > point[1] else overlap[1]
            else:
                overlap = point
                ans += 1
        
        return ans