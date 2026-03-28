# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int: 
        # since we have a nested function, we need to ensure that the value we are tracking/manipulating is mutable
        # or a reference type, in that case we use a list (as that is pass by reference)
        # if we wanted to use max_d as an int inside 'height' function then we utilize 'nonlocal' keyword in height method
        # like 'nonlocal max_d' at the start underneath 'height' method  
        max_d = [0]

        # the nested function to determine the maximum distance between any pair of nodes as we traverse the tree
        def height(root):
            # base case, since we calculate the distance then we will return 0
            if root is None:
                return 0
            
            # recursive step, go to left and right subtree
            left = height(root.left)
            right = height(root.right)
            # get the distance of left and right pair
            d = left + right
            # see the max distance, if we either have a new larger distance or not
            max_d[0] = max(max_d[0], d)

            # we return the height of a subtree as the current node + the height of the longest pathway under that subtree
            return 1 + max(left, right)
        
        # apply the nested function on the root, which will result in max_d[0] being manipulated
        height(root)
        # return max_d[0] which is the result of the diameter of the tree
        return max_d[0]
    
    # Run Time: O(N)
