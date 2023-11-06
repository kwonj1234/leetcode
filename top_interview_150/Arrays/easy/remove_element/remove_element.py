class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = len(nums) - 1
        nums_val = len(nums)

        while i <= j and i < len(nums) and nums[i] is not '_':
            if nums[i] == val:
                nums[i] = '_'
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
                nums_val -= 1

            else:
                i += 1
        
        return nums_val