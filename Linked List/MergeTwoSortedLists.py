"""
Eyal Haimovich
January 17, 2024

PROMPT:
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list.
The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

INTUITION:
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
ListNode has a val and a next, by using head = curr = ListNode(),
we assign the start of the list to head and parse the list with curr.
We compare list1.val to list2.val, set curr = list,
then go next with list = list.next, and curr = curr.next
finally, point to rest of list with curr.next = list.
Return head.next (head.val is placeholder) as pointer to start of merged list.

CONCLUSIONS:
if not list1 or not list2:
    return list1 or list2
head = curr = ListNode()

curr.next = list1 or list2
    return head.next

'if not' & 'return x or y' are very clean and useful syntax to remember.
remember to assign head to retain starting point of a linked list.
Logic is straight forward. Remember to .next both list and curr.
LinkedLists are ideal for removing items near start of list.
.pop is O(N) while head.next is O(1)
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # case a list is empty
        if not list1 or not list2:
            return list1 or list2

        head = curr = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        curr.next = list1 or list2
        return head.next


solution = Solution()

list1 = ListNode(1, ListNode(2, ListNode(3)))
list2 = ListNode(2, ListNode(3, ListNode(4)))
merged_list = solution.mergeTwoLists(list1, list2)

print('[', end="")  # remove \n
while merged_list:
    if merged_list.next:
        print(merged_list.val, end=",")
    else:  # no comma last num in list
        print(merged_list.val, end="")
    merged_list = merged_list.next
print(']')
