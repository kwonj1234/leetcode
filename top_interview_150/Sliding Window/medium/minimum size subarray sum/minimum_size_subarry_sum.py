class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # start = 0
        # total = 0
        # min_length = 0

        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         return 1
            
        #     total += nums[i]
        #     if total > target:
        #         while total > target:
        #             total -= nums[start]
        #             start += 1
            
        #     if total == target:
        #         if min_length == 0 or (i - start + 1) < min_length:
        #             min_length = i - start + 1
        
        # return min_length

        i, res = 0, len(nums) + 1
        for j in range(len(nums)):
            target -= nums[j]
            while target <= 0:
                res = min(res, j - i + 1)
                target += nums[i]
                i += 1
        return res % (len(nums) + 1)