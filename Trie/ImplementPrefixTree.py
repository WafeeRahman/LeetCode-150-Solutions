class TrieNode:
    def __init__(self):
        self.children = {} #26 Children for each letter in the alphabet
        self.isEndOfWord = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        rootPTR = self.root
        for char in word:
            if char not in rootPTR.children:
                rootPTR.children[char] = TrieNode()
            rootPTR = rootPTR.children[char]
        rootPTR.isEndOfWord = True
        

    def search(self, word: str) -> bool:
        rootPTR = self.root
        for char in word:
            if char not in rootPTR.children:
                return False
            rootPTR = rootPTR.children[char]
        return rootPTR.isEndOfWord
            
        
    def startsWith(self, prefix: str) -> bool:
        rootPTR = self.root
        for char in prefix:
            if char not in rootPTR.children:
                return False
            rootPTR = rootPTR.children[char]
        return True
            
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
