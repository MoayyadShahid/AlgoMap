# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # base case if root is Null then return True
        if root is None:
            return True

        # we need to validate the BST by comparing the previous with the current value
        prev = None
        
        # nested method to traverse the BST
        def traverse(root):
            # since we are using an outer-scope variable to track we need to declare 'nonlocal'
            nonlocal prev

            # base case, if root is Null, then we return True
            if root is None:
                return True
            # else we will do an in-order traversal
            else:
                # we do a quick check to see the left subtree fails, if not we continue
                if not traverse(root.left):
                    return False
                
                # we check the current value and see if it fails by having curr less than or equal to the previous 
                if prev is not None and root.val <= prev:
                    return False
                # set prevous to the current value
                prev = root.val

                # recurse on the right subtree
                return traverse(root.right)
        
        # use the root of the tree and do the in order traversal of the BST
        return traverse(root)
    
    # Run Time: O(N)
