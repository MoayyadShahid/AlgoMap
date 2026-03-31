# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if both trees are empty or have reached empty together, then they're equal
        if p is None and q is None:
            return True
        # if one tree is null while the other isn't then they aren't equal
        elif p is None or q is None:
            return False
        # otherwise we recurse on both trees
        else:
            # if the values are not equal then equality has failed
            if p.val != q.val:
                return False
            p_left, p_right = p.left, p.right
            q_left, q_right = q.left, q.right

            # we recurse on both the left AND right subtrees of both trees to determine
            # the equality of those subtrees
            # we need AND condition between both recursive calls for FAIL FAST procedure
            # if we encounter a false anywhere when recursing
            return self.isSameTree(p_left, q_left) and self.isSameTree(p_right, q_right)
    # Run Time: O(N)