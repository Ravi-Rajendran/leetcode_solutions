'''
Swap nodes in pairs
https://leetcode.com/problems/swap-nodes-in-pairs/description/
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def swapPairs(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if head is None or head.next is None:
        return head
    current = x = head
    while current is not None:
        if current.next is None:
            break
        next_node_value = current.next.val
        current.next.val = current.val
        current.val = next_node_value
        current = current.next.next
    return head

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
    head = swapPairs(head)
    printListNode(head)

main()
