class Solution:
    def isPalindrome(self, s: str) -> bool:

        # define the pointers
        left = 0
        right = len(s)-1

        while left < right:

            # while the character is NOT a letter or a number
            # keep moving the pointer inward
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            
            # check if the two characters match
            # fail fast check = Use whenever a problem requires perfection to be valid
            if s[left].lower() != s[right].lower():
                return False 

            # otherwise, if they do match, check the NEXT inner pair
            left += 1
            right -= 1

        return True






