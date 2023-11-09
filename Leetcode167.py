class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pointer1 = 0
        pointer2 = len(numbers) - 1
        while(pointer1 != pointer2):
            sum_ = numbers[pointer1] + numbers[pointer2]
            if  sum_ == target:
                return [pointer1 + 1, pointer2 + 1]
            elif sum_ < target:
                pointer1 += 1
            else:
                pointer2 -= 1