# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None:
            return None
        
        cur = head
        nodes = []
        
        while(cur.next != None):
            nodes.append(cur)
            cur = cur.next
        nodes.append(cur)
        
        i = len(nodes) - n

        if i == 0:
            return head.next
        elif i == (len(nodes) - 1):
            nodes[i-1].next = None
        else:
            nodes[i-1].next = nodes[i+1]
                
        return head