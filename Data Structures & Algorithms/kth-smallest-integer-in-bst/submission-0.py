# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        ans = -1

        def bfs(root):
            nonlocal ans, n
            if not root:
                return 
            bfs(root.left)
            n+=1
            if n==k: ans = root.val
            bfs(root.right)

        bfs(root)
        return ans

        