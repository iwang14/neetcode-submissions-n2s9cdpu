class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest_sequence = 0 # tracks the overall longest across all sequences
        

        for i in numSet:
            if i-1 not in numSet:
                length = 1 # current sequence you're counting right now
                while (i+length) in numSet:
                    length += 1
                if length > longest_sequence:
                    longest_sequence = length
        return longest_sequence
