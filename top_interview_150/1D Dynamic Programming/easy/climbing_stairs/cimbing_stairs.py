class Solution:
    def climbStairs(self, n: int) -> int:
        current_step, prev = 2, 1
        
        if n >= 3:
            for _ in range(3, n+1):
                prev, current_step = current_step, prev + current_step
        else:
            return n

        return current_step