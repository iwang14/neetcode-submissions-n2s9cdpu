from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
         # edge case
        if len(s1) > len(s2): return False
        
        # build frequency maps
        count1 = Counter(s1)             # target, never changes
        count2 = Counter(s2[:len(s1)])   # first window
        
        # how many chars already match before loop
        matches = sum(count1[c] == count2[c] for c in count1)
        
        for i in range(len(s1), len(s2)):
            # check if current window is a permutation
            if matches == len(count1): return True
            
            # add right char
            c = s2[i]
            count2[c] += 1
            if c in count1:
                if count2[c] == count1[c]:     matches += 1  # hit target
                elif count2[c] == count1[c]+1: matches -= 1  # overshot
            
            # remove left char
            left = s2[i - len(s1)]
            count2[left] -= 1
            if left in count1:
                if count2[left] == count1[left]:     matches += 1  # landed on target
                elif count2[left] == count1[left]-1: matches -= 1  # fell below target
        
        # check last window
        return matches == len(count1)