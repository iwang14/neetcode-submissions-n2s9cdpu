class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # map[key] = value  - how to add a key with a value
        # map[key] += 1 - increment an existing key 
        hashmap = {}

        #for i in range(nums): --> this gives the indices

    # The Frequency Map
        for num in nums:
            if(num not in hashmap):
                hashmap[num] = 1
            elif(num in hashmap):
                hashmap[num] += 1
        
           # Step 2 — create frequency slots
        freq = [[] for i in range(len(nums) + 1)]
        for num, count in hashmap.items():
            freq[count].append(num)
        
        # Step 3 — walk backwards, collect k elements
        result = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result


















