class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        low, fast = head, head
        while fast and fast.next:
            low = low.next
            fast = fast.next.next
        return low