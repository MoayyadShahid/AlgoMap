# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # quick check, if root is Null, return Null
        if root is None:
            return None
        
        # this will help us track the k
        track = [0]
        # this will help us track the actual value for k
        kthVal = [None]

        # this nested helper method will help us do an in-order traversal of BST
        def traverse(root):
            # base case, if root is None, then we return k
            if root is None:
                return k
            # otherwise if we have found the correct kth Value then we return right away
            elif kthVal[0] is not None:
                return None
            # otherwise we do in-order traversal
            else:
                # in order requires we do recurse left, process current, recurse right
                traverse(root.left)
                # we increment the tracker for k
                track[0] += 1
                # if the k tracker eqautes to k then we found the right node value
                if track[0] == k:
                    # set the value of the kth node
                    kthVal[0] = root.val 
                # recurse on the right node
                traverse(root.right)
    
        # use the nested helper method on the root        
        traverse(root)
        # return the actual value of the kth node
        return kthVal[0]
    
    # Run Time: O(N)
        