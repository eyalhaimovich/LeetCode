"""
Eyal Haimovich
January 22, 2024

PROMPT:
Given the head of a sorted linked list, delete all duplicates such
that each element appears only once. Return the linked list sorted as well.

Input: head = [1,1,2]
Output: [1,2]

Input: head = [1,1,2,3,3]
Output: [1,2,3]

INTUITION:
loop through the list until p.next doesn't exist
since sorted, need to only compare p.val to p.next.val
if equal, set p.next to p.next.next -- if doesn't exist, will just be None
else, forward p to p.next

CONCLUSIONS:
while p and p.next, checking both p and p.next, simplifies the loop a lot
Since p.next = p.next.next returns None if DNE, it works as we want without extra work
Only need to forward p if values aren't equal.
If they are equal, forwarding .next is enough.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteDuplicates(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    p = head  # maintain original header location
    while p and p.next:
        if p.val == p.next.val:
            p.next = p.next.next
        else:
            p = p.next
    return head


lnklist = ListNode(1, ListNode(3, ListNode(3, ListNode(5,None))))
head = deleteDuplicates(lnklist)

print("[", end="")
while head:
    print(f'{head.val},', end='')
    head = head.next
print("]")
