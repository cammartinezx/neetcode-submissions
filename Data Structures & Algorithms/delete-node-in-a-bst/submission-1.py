# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        #search for the value
        if root.val > key:
            root.left = self.deleteNode(root.left,key)
        elif root.val < key:
            root.right = self.deleteNode(root.right,key)
        #if found the node
        else:
            #if node has only one children
            if not root.right:
                return root.left
            if not root.left:
                return root.right
            #if node has 2 children
            #find min from right subtree
            curr =root.right
            while curr.left:
                curr=curr.left
            #assign that value to the node to delete
            root.val=curr.val
            #delete the node
            root.right = self.deleteNode(root.right, curr.val)
        return root

        