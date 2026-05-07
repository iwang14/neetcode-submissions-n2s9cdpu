class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1 = {}

        # build a dictionary
        # map each key to a list as its value
        # list contains all anagrams matching that key
        # return all the values of the dict in an array

        for i in range(len(strs)):
            key = "".join(sorted(strs[i]))
            if key not in dict1:
                dict1[key] = []
            dict1[key].append(strs[i])
        return list(dict1.values()) # return list of anagrams


            #if strs[i] not in dict1:
                # dict1 = strs[i] --> this overwrites entire dict1
                # dict1[strs[i]] = []

            # if the key is not currently in dict1, add a new key value pair, with value being an empty array
            # if key not in dict1:
                #dict1[key] = []

            # strs[i] == dict1[strs[i]]
            # dict1[strs[i]] = strs[i]
            # key = "".join(sorted(strs[i]))
            # if key in dict1:
                # dict1[key]=strs[i]
                # dict1[key].append(strs[i])






