"""
Eyal Haimovich
January 23, 2024

PROMPT:
Given the root of a binary tree, return the
inorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [1,3,2]

INTUITION:
Left -> node -> right
Inorder is leftmost to rightmost.
Go down left branch while retaining each root in stack
add last root to output and set root to previous node
attempt root.right, if none, repeat until root and stack are clear

CONCLUSIONS:
Inorder:  Left -> node -> right
1) keep track of roots using stack
2) while root or stack // while root work well together.
    root = root.right makes root none, skipping repeated root.left loop
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorderTraversal(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    result, stack = [], []

    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        result.append(root.val)
        root = root.right
    return result

# sample binary tree
#        1
#       / \
#      2   3
#     / \
#    4   5


# Creating nodes
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)

# Connecting nodes to form the binary tree
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5

# Performing inorder traversal on the binary tree
result = inorderTraversal(node1)
print(result)
