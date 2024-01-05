class Solution:
    def rob(self, nums: List[int]) -> int:
        max_money = 0
        for i in range(len(nums)):
            a, b = 0, 0
            if i >= 2:
                a = nums[i] + nums[i-2]
            if i >= 3:
                b = nums[i] + nums[i-3]

            nums[i] = max(a,b,nums[i])
            max_money = max(nums[i], max_money)

        return max_money