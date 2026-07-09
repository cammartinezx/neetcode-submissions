# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #space O(w)xO(n) for the result so o(n) TIME O(n)
        total = []
        if root is None:
            return total
        
        queue = deque([root])
        while queue:
            size_level = len(queue)
            curr_level = []
        
        #for each level
            for i in range(size_level):
                curr = queue.popleft()
                curr_level.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right) 

            total.append(curr_level)

        return total    