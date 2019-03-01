# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Example:
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = cur = ListNode(0)
        carry = 0
        while l1 and l2:
            digit_sum = l1.val + l2.val + carry
            cur.next = ListNode(digit_sum%10) # insert n%10 in the node
            print(digit_sum%10)
            cur = cur.next
            carry = digit_sum//10 # n//10 is the carry over
            l1 = l1.next
            l2 = l2.next
        return dummy.next

a = ListNode(7)
b = ListNode(7)
c = ListNode(7)
a.next = b
b.next = c

print(Solution().addTwoNumbers(a, a))

