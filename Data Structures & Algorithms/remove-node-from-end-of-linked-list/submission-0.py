# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = []

        curr = head

        while curr:
            nodes.append(curr)
            curr = curr.next
        
        node_to_remove = len(nodes) - n

        if node_to_remove == 0:
            return head.next

        nodes[node_to_remove - 1].next = nodes[node_to_remove].next

        return head
        