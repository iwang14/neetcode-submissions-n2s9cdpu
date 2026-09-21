class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles)
        best = hi # max(piles) always works, so it's a safe default

        while lo <= hi:
            mid = (lo + hi) // 2   # guess for k

            hours = 0
            for p in piles:
                hours += math.ceil(p / mid)

            if hours <= h:   # fast enough: save it, try slower
                best = mid
                hi = mid - 1
            else:             # too slow: go faster
                lo = mid + 1

        return best