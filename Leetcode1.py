class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        difference = {}
        for i,n in enumerate(nums):
            if n in difference:
                return difference[n],i
            else:
                difference[target-n] = i