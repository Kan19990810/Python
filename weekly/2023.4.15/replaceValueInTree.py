class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        """
        class Solution:

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        results = []
        if not root:
            return results

        from collections import deque
        que = deque([root])

        while que:
            size = len(que)
            result = []
            for _ in range(size):
                cur = que.popleft()
                result.append(cur.val)
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
            results.append(result)

        return results
        """
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        from collections import deque

        que = deque([root])

        while que:
            print(que)
            size = len(que)
            num = []
            for i in range(size):
                cur = que.popleft()
                num.append(cur.val)
                if cur.left and cur.right:

                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
        return root

