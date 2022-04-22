# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h = [(n.val, i, n) for i,n in enumerate(lists) if n]
        print(h)
        heapify(h)
        dummy = node = ListNode()
        while h:
            v, i, n = h[0]
            if n.next == None:
                heappop(h)
            else:
                heapreplace(h, (n.next.val, i, n.next))
            node.next = n
            node = node.next
        return dummy.next

        
        
        
            