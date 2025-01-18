class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Bucket Sort
        counts = {}
        #Buckets will have a bucket for every possible count
        #Which ranges from 1-n inclusive
        buckets= [[] for i in range(len(nums)+1)]
        res = []
        
        #Populate Counts
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        

        #For Every Number and its associated count
        for key in counts.keys():
            print(
                counts[key], key, buckets
            )

            #Add the number with the count in its slot at bucket[count]
            buckets[counts[key]].append(key)
        
        #Go from greatest counts to least count to get the most frequent elements
        for i in range(len(buckets)-1, -1,-1):
            if not(buckets[i]):
                continue
            for j in range(len(buckets[i])):
                #When result == k in length, we found the top k most frequent elements
                if len(res) == k:
                    return res
                res.append(buckets[i][j])
        
        return res
        
        
            
