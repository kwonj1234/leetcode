# Time Limit Exceeded, brute force solution
# class Solution:
#     def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
#         for i in range(len(gas)):
#             # if this is a potential starting point check if it works
#             if gas[i] >= cost[i]:
#                 tank = gas[i]
#                 j = i
#                 for _ in range(len(gas)):
#                     j += 1
#                     if j >= len(gas):
#                         j = 0
                    
#                     tank -= cost[j-1]
#                     if tank < 0:
#                         break
#                     else:
#                         tank += gas[j]
                        
#                 if tank > 0:
#                     return i
#         return -1

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n, total_surplus, surplus, start = len(gas), 0, 0, 0
        
        for i in range(n):
            total_surplus += gas[i] - cost[i]
            surplus += gas[i] - cost[i]
            if surplus < 0:
                surplus = 0
                start = i + 1
        return -1 if (total_surplus < 0) else start
