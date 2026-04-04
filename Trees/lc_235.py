# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # we will use this to track the lowest common ancestor treeNode
        lca = root
        
        # quick check to see if we have a Null root, then we just return nothing
        if not root:
            return
        
        # nested helper method to traverse the BST to find the LCA
        # we have 3 cases basically:
        # 1. either both p and q are less than root, so we go left subtree to find lca
        # 2. either both p and q are greater than root, so we go right subtree to find lca
        # 3. else p and q are split on the root so we found our lca
        def search(root):
            # declare outer-scope variable as nonlocal to be able to track lca
            nonlocal lca

            # base case, if root is Null return nothing
            if not root:
                return
            # if both p and q are greater than root then we go to right subtree and recurse
            if root.val < p.val and root.val < q.val:
                return search(root.right)
            # if both p and q are less than root then we go to left subtree and recurse
            elif root.val > p.val and root.val > q.val:
                return search(root.left)
            # otherwise p and q will be split on the root, so we found our lca
            else:
                lca = root
        
        # apply the nested helper method to search on the root of the tree
        search(root)
        # return the lca
        return lca

    # Run Time: O(N)
