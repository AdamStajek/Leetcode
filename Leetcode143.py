# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        size = 0
        cur = head
        while (cur):
            size += 1
            cur = cur.next

        if size < 3:
            return head

        cur = head
        for i in range(int(size / 2)):
            cur = cur.next

        new_head = cur.next
        cur.next = None

        # reverse the second list

        new = new_head
        cur = new_head.next
        new_head.next = None
        while (cur):
            next_ = cur.next
            cur.next = new
            new = cur
            cur = next_
        new_head = new

        # merge lists
        dummy = ListNode()
        cur = dummy
        cur1 = head
        cur2 = new_head
        i = 0
        while (cur1 and cur2):
            if i % 2 == 0:
                cur.next = cur1
                cur1 = cur1.next
            else:
                cur.next = cur2
                cur2 = cur2.next
            cur = cur.next
            i += 1
        if cur2 == None:
            cur.next = cur1
        else:
            cur.next = cur2

        head = dummy.next

