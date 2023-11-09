from math import ceil


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def time(k):
            cur_time = 0
            for amount in piles:
                cur_time += ceil(amount / k)
            return cur_time

        left, right = 1, max(piles)
        k = right

        while left <= right:
            mid = (left + right) // 2
            if time(mid) > h:
                left = mid + 1
            elif time(mid) <= h:
                k = mid
                right = mid - 1

        return k




