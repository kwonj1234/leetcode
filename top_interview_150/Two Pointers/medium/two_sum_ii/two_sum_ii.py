# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         for i in range(len(numbers)):
#             for j in range(i+1, len(numbers)):
#                 if numbers[i] + numbers[j] == target:
#                     return [i+1, j+1]
#                 elif numbers[j] > target - numbers[i]:
#                     break

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1

        while numbers[i] + numbers[j] != target:
            if numbers[i] + numbers[j] < target:
                i += 1
            elif numbers[i] + numbers[j] > target:
                j -= 1

        return [i+1, j+1] 