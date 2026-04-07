# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res=0

        def maxheight(root):
            if not root:
                return 0
            leftmax=maxheight(root.left)
            rightmax=maxheight(root.right)

            self.res=max(self.res,leftmax+rightmax)
            return 1 + max(leftmax,rightmax)
        maxheight(root)
        return self.res