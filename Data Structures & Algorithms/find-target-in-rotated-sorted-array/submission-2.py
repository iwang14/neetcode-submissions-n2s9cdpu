class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left,right = 0, len(nums)-1

        # keep going while window has at least 1 element 
        while left<=right:

            # middle of the current window
            mid = (left+right)//2

            # land right on the target
            if nums[mid] == target:
                return mid

            # values go up from left to mid -> no seam there -> left half is sorted 
            if nums[left] <= nums[mid]:

                # sorted half lets us do a range check 
                # (<nums[mid] is strict because we already checked mid)
                if nums[left] <= target < nums[mid]:

                    # target is in the left half -> drop right half 
                    right = mid - 1
                
                else:

                    #not in the left half -> it can only be on the right
                    left = mid + 1

            #otherwise the seam is in the left half -> right half is sorted
            else:
                
                # range check on the sorted right half
                # (> nums[mid] is strict for same reason)

                if nums[mid] < target <= nums[right]:

                    # target is in right half -> drop left half
                    left = mid + 1
                else:
                    # not in right half -> it can only be on the left
                    right = mid - 1
        return -1















