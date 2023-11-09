class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        if left == right or nums[len(nums) - 1] > nums[0]:
            return nums[0]

        while left != right:
            mid = (left + right) // 2
            if nums[mid] > nums[left]:
                left = mid
            elif nums[mid] <= nums[left]:
                right = mid
        return nums[left + 1]

