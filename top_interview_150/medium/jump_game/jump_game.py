# Bad Solution that uses recursion but runs out of time
# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         def recursion(i: int):
#             if i == len(nums) - 1:
#                 return True

#             for j in range(1, nums[i] + 1):
#                 if recursion(i+j):
#                     return True

#             return False

#         return recursion(0)

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reachable = 0

        for i in range(len(nums)):

            if i>reachable:
                return False  

            reachable = max(reachable, i+nums[i])
            
        return True