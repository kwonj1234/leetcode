# # BAD BRUTE FORCED
# class Solution:
#     def candy(self, ratings: List[int]) -> int:
#         candies = [1 for _ in range(len(ratings))]

#         for i in range(len(ratings)):
#             change = False
#             if i+1 < len(ratings):
#                 if ratings[i] > ratings[i+1] and candies[i] <= candies[i+1]:
#                     candies[i] = candies[i+1] + 1
#                     change = True
#             if i-1 >= 0:
#                 if ratings[i] > ratings[i-1] and candies[i] <= candies[i-1]:
#                     candies[i] = candies[i-1] + 1
#                     change = True

#             if change:
#                 for j in reversed(range(i)):
#                     if j+1 < len(ratings):
#                         if ratings[j] > ratings[j+1] and candies[j] <= candies[j+1]:
#                             candies[j] = candies[j+1] + 1
#                     if j-1 >= 0:
#                         if ratings[j] > ratings[j-1] and candies[j] <= candies[j-1]:
#                             candies[j] = candies[j-1] + 1
#         return sum(candies)

# Greedy Algorithm
# class Solution:
#     def candy(self, ratings: List[int]) -> int:
#         n = len(ratings)
#         candies = [1] * n 

#         for i in range(1, n):
#             if ratings[i] > ratings[i-1]:
#                 candies[i] = candies[i-1] + 1

#         for i in range(n-2, -1, -1):
#             if ratings[i] > ratings[i+1]:
#                 candies[i] = max(candies[i], candies[i+1] + 1)
        
#         return sum(candies)

class Solution:
    def candy(self, ratings: List[int]) -> int:
        if not ratings:
            return 0
        
        ret, up, down, peak = 1, 0, 0, 0
        
        for prev, curr in zip(ratings[:-1], ratings[1:]):
            if prev < curr:
                up, down, peak = up + 1, 0, up + 1
                ret += 1 + up
            elif prev == curr:
                up = down = peak = 0
                ret += 1
            else:
                up, down = 0, down + 1
                ret += 1 + down - int(peak >= down)
        
        return ret