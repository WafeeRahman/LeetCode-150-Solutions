class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word):
        rootPTR = self.root
        for char in word:
            if char not in rootPTR.children:
                rootPTR.children[char] = TrieNode()
            rootPTR = rootPTR.children[char]
        rootPTR.isEndOfWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        prefixTrie = Trie()
        
        for word in words:
            prefixTrie.addWord(word)
        
        ROWS, COLS = len(board), len(board[0])
        res = set()    
        #Traverse PrefixTrie to find all words w/ prefixes while not visiting the same cells
        def dfs(r,c, prefixTrie, curWord):

            if (min(r,c) < 0 
               or r >= ROWS or c >= COLS
               or board[r][c] not in prefixTrie.children
               or board[r][c] == ".") :
               return 
            #If the current character is a valid letter in one of the words we have in the prefix tree
            #Visit and add it the currently build word
            char = board[r][c]
            
            prefixTrie = prefixTrie.children[char]
            
            curWord += char
            
            #Mark as visited
            board[r][c] = "."

            #If we reached the end of a valid word, add the currently built word to res set
            #That way duplicates are handled
            if prefixTrie.isEndOfWord:
                res.add(curWord)
            
            dirs = [[0,1], [0,-1], [1, 0], [-1,0]]
            #Visit Adjacent Cells
            for dr, dc in dirs:
                nr, nc = r+dr,c+dc
                dfs(nr,nc,prefixTrie,curWord)
            
            #Unvisit to BackTrack
            board[r][c] = char
            return
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c,prefixTrie.root,"")
        
        return list(res)

            




                        


        

            
            

            


        
        
