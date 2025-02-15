class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode() #Trie Implmentation for each word with glob searching

    #Add words character by character in trie
    def addWord(self, word: str) -> None:
        rootPTR = self.root
        for char in word:
            if char not in rootPTR.children:
                rootPTR.children[char] = TrieNode()
            rootPTR = rootPTR.children[char]
        rootPTR.isEndOfWord = True
        

    def search(self, word: str) -> bool:
        #To search all possible characters if we encounter a ".", we need to run a dfs on all character children
        def dfs(root, i):
            if i == len(word):
                return root.isEndOfWord
            #If theres a glob, we try to match the end of the word to start at any child of the current letter
            #If no child of the current letter returns a valid word at "." the "." is invalid
            if word[i] == '.':
                for child in root.children:
                    if dfs(root.children[child], i+1):
                        return True
                return False 
            
            #If the next letter is not a child of the current trienode then we cant continue search
            if word[i] not in root.children:
                return False
            #OTWS traverse the trie
            root = root.children[word[i]]
            
            #OTWS continue search until we reach a base case
            return dfs(root, i+1)
        
        return dfs(self.root, 0)


        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
