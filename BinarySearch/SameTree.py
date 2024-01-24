"""
Eyal Haimovich
January 23, 2024

PROMPT:
Given the roots of two binary trees p and q,
write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally
identical, and the nodes have the same value.

Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false

INTUITION:
create a stack for both p and q and loop through them
loop until stackp or p or stackq or q are all empty
test if p or q for structure
test if p.val != q.val for equallity
once loop done, check if p or q remains (if so not equal)

CONCLUSIONS:
recursive may be a clearer approach with base conditions
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSameTree(p, q):
    """
    :type p: TreeNode
    :type q: TreeNode
    :rtype: bool
    """
    stackp = []
    stackq = []
    while stackp or p or stackq or q:
        while p and q:
            stackp.append(p)
            stackq.append(q)
            p = p.left
            q = q.left
        if p or q:  # case structure mismatch
            return False
        p = stackp.pop()
        q = stackq.pop()
        if p.val != q.val:  # case val not equal
            return False
        p = p.right
        q = q.right
    if p or q:  # case both trees aren't clear
        return False
    else:
        return True


def recursiveIsSameTree(p, q):
    # Base case: If both trees are empty, they are identical.
    if not p and not q:
        return True
    # If one of the trees is empty and the other is not, they are not identical.
    if not p or not q:
        return False

    # Compare the values of the current nodes.
    if p.val != q.val:
        return False

    # Recursively check the left and right subtrees.
    return recursiveIsSameTree(p.left, q.left, ) and recursiveIsSameTree(p.right, q.right, )


# Example 1
# Tree 1:    1
#           / \
#          2   3
# Tree 2:    1
#           / \
#          2   3
tree1 = TreeNode(1, TreeNode(2), TreeNode(3))
tree2 = TreeNode(1, TreeNode(2), TreeNode(3))

result1 = isSameTree(tree1, tree2)
print("Example 1 iter Result:", result1)
result1 = recursiveIsSameTree(tree1, tree2)
print("Example 1 rec Result:", result1)

# Example 2
# Tree 3:    1
#           / \
#          2   3
# Tree 4:    1
#           / \
#          2   4
tree3 = TreeNode(1, TreeNode(2), TreeNode(3))
tree4 = TreeNode(1, TreeNode(2), TreeNode(4))

result2 = isSameTree(tree3, tree4)
print("Example 2 iter Result:", result2)
result2 = recursiveIsSameTree(tree3, tree4)
print("Example 2 rec Result:", result2)
