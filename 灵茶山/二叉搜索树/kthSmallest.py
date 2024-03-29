class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        orderList = []

        def orderRoot(root):
            if not root:
                return

            orderRoot(root.right)

            nonlocal orderList
            orderList.append(root.val)

            orderRoot(root.left)

        orderRoot(root)

        return orderList[k - 1]

