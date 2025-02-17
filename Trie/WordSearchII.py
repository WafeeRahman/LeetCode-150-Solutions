#With an mxn board of characters, and a list of words, we need to return all words that appear in the board
#Each word is built from adjacent cells (horizontal or vertical), we can't visit the same letter twice for a word path, but we can
#Continue from it (ie, oa oaa are in the list of words and adjacent in the board)

#We can use DFS to search each character
#Use a prefix trie to keep the prefixes of each word character by character
#Where we can traverse the tree each time an adjacent character belongs to a child of the current prefix trie node
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
        res = set() #We may encounter duplicates in DFS, and we know each word in words is unique, so we can maintain a solution set
        ROWS = len(board)
        COLS = len(board[0])
        
        #After feeding words into the trie, we can traverse the trie for each character we find that is in the trie
        #Building a word character by character, and if we build a word, we can add to solution set
        def dfs(r, c, root, curWord):
            #If we're out of bounds, or the current character isnt a valid next character in trie
            #Or if we already visited the current cell, we dont want to continue
            if (min(r,c) < 0 
                or r >= ROWS or c >= COLS
                or board[r][c] == "."
                or board[r][c] not in root.children):
                return
            
            #OTWS we can traverse this cell
            char = board[r][c]
            root = root.children[char]
            curWord += char
            board[r][c] = "."

            #If we reached the end of a word
            if root.isEndOfWord:
                res.add(curWord)
                #Even if the current letter is the end of a word, it may have children to build more words
                #Continue search

            #adjacent dirs
            dirs= [[0,1], [0,-1], [1,0], [-1,0]]
            for dr, dc in dirs:
                nr, nc = r+dr, c+dc
                dfs(nr,nc,root,curWord)
            #After visiting all adjacent cells, backtrack and unvisit
            board[r][c] = char
            return
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c,prefixTrie.root,"")
        return list(res)

            



        
