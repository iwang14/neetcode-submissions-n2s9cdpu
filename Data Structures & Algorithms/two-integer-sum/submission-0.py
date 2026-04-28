from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        number_tracker_dict = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in number_tracker_dict:
                return [number_tracker_dict[complement], i]
            number_tracker_dict[nums[i]] = i



        #  number_tracker_dict = defaultdict(int)

        # for i in range len(nums):
        #     number_tracker_dict[i+1] += 1 

        #     if nums[i]+number_tracker_dict[i+1] == target:
        #         return True
        #     else:
        #         return False