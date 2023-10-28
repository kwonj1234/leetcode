class Solution:
    def jump(self, nums: List[int]) -> int:
        ans = 0
        pointer = 0
        farthest = 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i]):

            if farthest >= len(nums) - 1:
                ans += 1
                break
            elif i == pointer:
                ans += 1
                pointer = farthest
        
        return ans