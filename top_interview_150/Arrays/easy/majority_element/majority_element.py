# Example of the Boyer-Moore Majority Vote Algorithm

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 1
        current_num = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == current_num:
                count += 1
            elif count is 0:
                current_num = nums[i]
                count = 1
            elif nums[i] != current_num:
                count -= 1

        return current_num