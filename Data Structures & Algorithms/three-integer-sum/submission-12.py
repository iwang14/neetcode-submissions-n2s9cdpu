class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = []
        
        # enumerate() = (index, value)
        # append()

        for i in range(len(nums)):
            if nums[i]>0:
                return answer
            # checking for duplicates
            if i>0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = len(nums)-1

            # edge case: returning nothing (empty array)
            # if all the #'s are positive, then we're returning the empty array
            # if nums[i]>0:
            #     return answer

            while left < right:
                sum1 = nums[i] + nums[left] + nums[right]

                if sum1 > 0:
                    right -= 1
                elif sum1 < 0:
                    left += 1
                else:
                    answer.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1 
                    while left<right and nums[left] == nums[left-1]:
                        left += 1
                    #nums[right] == nums[right+1]
        return answer
















