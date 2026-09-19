# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        listN = head
        while listN and listN.next:
            if listN.val == listN.next.val:
                listN.next = listN.next.next
            else:
                listN = listN.next

        return head