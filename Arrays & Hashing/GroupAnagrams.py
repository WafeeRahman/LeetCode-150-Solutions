class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        anagrams = defaultdict(list)

        for word in strs:
            #With each word, if theres an anagram, they will have the same characters in sorted
            #Order as another
            #With this, we can use a hashmap (defaultdict with an empty list set as default value)
            #To add any anagrams for each word in strs as per the key, which is their sorted character sequence
            sort = ''.join(sorted(word))
            anagrams[sort].append(word)
        
        #Add each anagram sublist to result
        for anagram in anagrams.keys():
            res.append(anagrams[anagram])
        
        return res
        
        
