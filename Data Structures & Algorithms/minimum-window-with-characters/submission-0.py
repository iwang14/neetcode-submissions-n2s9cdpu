class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        need = {}
        for c in t:
            need[c] = need.get(c, 0) + 1

        have = {}
        have_count = 0           # # of distinct chars currently fully satisfied
        need_count = len(need)   # # of distinct chars we must satisfy

        res, res_len = [-1, -1], float("inf")
        left = 0

        for right in range(len(s)):
            c = s[right]
            have[c] = have.get(c, 0) + 1

            if c in need and have[c] == need[c]:
                have_count += 1

            # window is VALID -> shrink while it stays valid
            while have_count == need_count:
                if (right - left + 1) < res_len:        # measure HERE, while valid
                    res = [left, right]
                    res_len = right - left + 1

                have[s[left]] -= 1
                if s[left] in need and have[s[left]] < need[s[left]]:
                    have_count -= 1                     # we just broke validity
                left += 1

        l, r = res
        return s[l:r+1] if res_len != float("inf") else ""