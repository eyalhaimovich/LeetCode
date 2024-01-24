"""
Eyal Haimovich
January 24, 2024

PROMPT:
Given the root of a binary tree, check whether it is a mirror of itself
(i.e., symmetric around its center).

Example 1:
Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:
Input: root = [1,2,2,null,3,null,3]
Output: false

INTUITION:
Recursive feels most intuitive.
use dfs to traverse and compare l.left to r.right and l.right to r.left
2 base conditions:
if l and r:
    1) l.val == r.val keep looping
if not (l and r):
    2) if l == r (none == none) return true, else false.

CONCLUSIONS:
Determining false/true conditions is paramount
in recursion, l == r allows for checking both equality and none.
    none == none is true even if not l and not r
in iterative, stack = [(root.left, root.right)] retains the pairing.
    l, r = stack.pop() works by maintaining the mirror tuple.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def recursiveIsSymmetric(root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    return dfs(root.left, root.right)


def dfs(l, r):
    if l and r:
        return (l.val == r.val and dfs(l.left, r.right) and
                dfs(l.right, r.left))
    return l == r


def iterativeIsSymmetric(root):
    if not root:
        return True
    stack = [(root.left, root.right)]
    while stack:
        l, r = stack.pop()
        if not l and not r:
            continue
        if not l or not r:
            return False
        if l.val != r.val:
            return False
        stack.append((l.left, r.right))
        stack.append((l.right, r.left))
    return True


# Tree 1
# Symmetric Tree:
#         1
#       /   \
#      2     2
#     / \   / \
#    3   4 4   3
better_tree1 = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))

# Tree 2
# Non-Symmetric Tree:
#         1
#       /   \
#      2     2
#       \     \
#        3     3
better_tree2 = TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3)))

# Testing recursiveIsSymmetric and iterativeIsSymmetric
result_recursive1 = recursiveIsSymmetric(better_tree1)
result_iterative1 = iterativeIsSymmetric(better_tree1)
print("Tree 1 - Recursive Result:", result_recursive1)
print("Tree 1 - Iterative Result:", result_iterative1)

result_recursive2 = recursiveIsSymmetric(better_tree2)
result_iterative2 = iterativeIsSymmetric(better_tree2)
print("Tree 2 - Recursive Result:", result_recursive2)
print("Tree 2 - Iterative Result:", result_iterative2)
