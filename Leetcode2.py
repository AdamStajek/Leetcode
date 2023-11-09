# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        number = []
        left = 0
        cur1 = l1
        cur2 = l2
        while cur1 and cur2:
            x = cur1.val + cur2.val + left
            if x >= 10:
                number.append(x - 10)
                left = 1
            else:
                number.append(x)
                left = 0
            cur1 = cur1.next
            cur2 = cur2.next

        while cur1:
            x = cur1.val + left
            if x >= 10:
                number.append(x - 10)
                left = 1
            else:
                number.append(x)
                left = 0
            cur1 = cur1.next

        while cur2:
            x = cur2.val + + left
            if x >= 10:
                number.append(x - 10)
                left = 1
            else:
                number.append(x)
                left = 0
            cur2 = cur2.next

        if left == 1:
            number.append(1)

        head = ListNode()
        head.val = number[0]
        cur = head
        for num in number[1:]:
            cur.next = ListNode()
            cur = cur.next
            cur.val = num

        return head




