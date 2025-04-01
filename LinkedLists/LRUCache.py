class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None 
        self.prev = None 
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} #Store Nodes w/ Key Vals
        self.left = ListNode(0,0)
        self.right = ListNode(0,0)
        #Pointer to Least Recent (Right), Most Recent (Left)
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, key: int) -> int:
        cache = self.cache
        if not key in self.cache:
            return -1
        
        #After Lookup we need to place the node in the correct position
        node = cache[key]
        self.remove(node)
        
        #Once Looked Up Reset Cache and Move into Most Recent Position
        nxt = self.left.next
        self.left.next = node
        node.prev = self.left
        node.next = nxt
        nxt.prev = node

        #Set Cache Again As Remove Deletes It
        cache[node.key] = node
        return cache[node.key].val       

    #Remove Value From Current Position     
    def remove(self, node):
        cache = self.cache
        del(cache[node.key])
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev 
    
    def put(self, key: int, value: int) -> None:
        cache = self.cache
        #We don't wanna prematurely remove the LRU value if the key is not net new
        if len(cache) == self.cap and key not in cache:
            self.remove(self.right.prev)
            
        if key in self.cache:
            self.remove(cache[key])
        
        #Insert into most recent lookup position
        node = ListNode(key, value)
        cache[key] = node
        nxt = self.left.next
        self.left.next = node
        node.prev = self.left
        node.next = nxt
        nxt.prev = node 
    

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)    
