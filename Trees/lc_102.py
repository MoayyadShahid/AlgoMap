# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # if root/tree is Null then return empty list
        if root is None:
            return []
        
        # nested helper method, we track the node we are on 'root', we have the array which we will use to track the level nodes 'arr'
        # and then we will use the 'row' to track the level we are on and help us to add to 'arr' accordingly
        def level(root, arr, row):
            # if root/tree is null return None/Null
            if root is None:
                return None

            # if we are on a level and a dedicated sub-array doesn't exist we append it
            if len(arr) <= row:
                arr.append([])
            # we recurse on the left and right nodes of the the root/tree
            level(root.left, arr, row + 1)
            level(root.right, arr, row + 1)
            # we add the value of the current root/node value at the specific row-level sub-array at the respective row-index 'row'
            arr[row].append(root.val)
            # at the very end we return the arr once recursive unwinding is done
            return arr
        
        # we use the nested function with the base values
        return level(root, [], 0)
    # Run Time: O(N)
