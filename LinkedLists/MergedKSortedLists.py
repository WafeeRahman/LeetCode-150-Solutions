# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #Merge Lists Two at A Time
        def mergeTwoLists(l1, l2):
            dummy = ListNode(0)
            nl = dummy

            while l1 and l2:
                if l1.val < l2.val:
                    nl.next = l1
                    nl = nl.next
                    l1 = l1.next
                else:
                    nl.next = l2
                    l2 = l2.next
                    nl = nl.next
            if l1:
                nl.next = l1
            if l2:
                nl.next = l2
            
            return dummy.next
        
        if not lists:
            return None

        mergedLists = lists
        #Merge Down Lists Pair By Pair Until they are one sorted linked list
        while len(mergedLists) > 1:
            merged = []
            for i in range(0, len(mergedLists)-1, 2):
                l1 = mergedLists[i]
                l2 = mergedLists[i+1]
                merged.append(mergeTwoLists(l1, l2))\
            #If we have an odd amount of lists, the last will not be merged, add it to the next merge
            if len(mergedLists) % 2 == 1:
                merged.append(mergedLists[-1])
            mergedLists = merged
        return mergedLists[0]
            
        
    


   
