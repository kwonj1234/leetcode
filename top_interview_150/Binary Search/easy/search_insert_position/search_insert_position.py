class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        pivot = n//2
        start = 0
        end = n

        while True:
            if nums[pivot] == target:
                return pivot
            elif pivot == 0 and nums[pivot] > target:
                return 0
            elif pivot == n-1 and nums[pivot] < target:
                return n
            elif nums[pivot] < target < nums[pivot+1]:
                return pivot + 1
            elif nums[pivot-1] < target < nums[pivot]:
                return pivot

            elif nums[pivot] > target:
                end = pivot
                pivot = (pivot - start) // 2
            elif nums[pivot] < target:
                start = pivot
                pivot = ((end - pivot) // 2) + pivot