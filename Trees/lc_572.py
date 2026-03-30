# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # helper method to see if 2 trees are equal
    def same(self, p, q):
        # base case, if both are null then we have equality
        if p is None and q is None:
            return True
        # if one is null but the other isn't then we don't have equality
        elif p is None or q is None:
            return False
        # else if both are not Null then we need to recurse
        else:
            # we check if the values are the same and then we recurse on the left and right trees of both
            return p.val == q.val and self.same(p.left, q.left) and self.same(p.right, q.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # base case, we check if both the tree and subtree are null, if so then we have subset
        if root is None and subRoot is None:
            return True
        # otherwise if only the tree is Null but the subtree, then we can't have a subtree
        elif root is None:
            return False
        # else both are not null, we check 3 things
        # 1. if the tree is equal to the subtree
        # 2. recurse and see if the left subtree of the tree is equivalent to target subtree
        # 3. recurse and see if the right subtree of the tree is equivalen to target subtree
        else:
            return self.same(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
    # Run Time: O(N)
