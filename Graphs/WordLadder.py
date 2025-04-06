class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adj = defaultdict(list)
        
        #Create An Adjacency List Based On Words (From WordList) that can be reached with a single 
        #Letter Character replacement for each character in word, for each word in the wordlist
        for word in wordList:
            for i in range(len(word)):
                charReplacement = word[:i] + "*" + word[i+1:]
                adj[charReplacement].append(word)
        

        #Let's Use BFS to get the shortest path from beginWord to endWord
        q = deque([beginWord])
        visit = set()
        visit.add(beginWord)
        transformationCount = 1
        while q:
            #Level Order Traversal
            for i in range(len(q)):
                word = q.popleft()
                
                if word == endWord:
                    return transformationCount
                
                for i in range(len(word)):
                    charReplacement = word[:i] + "*" + word[i+1:]
                    for adjWord in adj[charReplacement]:
                        if adjWord not in visit:
                            q.append(adjWord)
                            visit.add(adjWord) #Visit New Words
            
            transformationCount += 1
        
        return 0 
