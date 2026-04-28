from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters_dict_s = defaultdict(int)
        letters_dict_t = defaultdict(int)

        for letter in s:
            letters_dict_s[letter] +=1
        for letter in t:
            letters_dict_t[letter] +=1

        if letters_dict_s == letters_dict_t:
            return True
        else:
            return False