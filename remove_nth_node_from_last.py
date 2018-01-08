'''
Remove the nth node from the end of the last.
https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def removeNthFromEnd(head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    if head is None:
        return head

    head_copy = ListNode('/')
    head_copy.next = head
    forward = follow = head_copy
    for _ in range(n):
        forward = forward.next

    # print(forward.val)
    while forward.next is not None:
        print(forward.val, follow.val)
        forward = forward.next
        follow = follow.next

    # print('=>', forward.val, follow.val)
    follow.next = follow.next.next
    return head_copy.next


def printListNode(head):
    cur = head
    while cur:
        print(cur.val, end=' ')
        cur = cur.next
    print()


def main():
    array = [1, 2, 3, 4, 5]
    head = l = ListNode('/')
    for i in array:
        l.next = ListNode(i)
        l = l.next
    head = head.next
    printListNode(head)
    head = removeNthFromEnd(head, 5)
    printListNode(head)

main()
