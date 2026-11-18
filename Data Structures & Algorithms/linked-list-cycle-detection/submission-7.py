# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        curr = head
        future = curr.next
        while curr.next:
            if curr == future:
                return True
            if future.next == None or future.next.next == None:
                return False
            
            future = future.next.next
            curr = curr.next
        return False



