# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @staticmethod
    def build_linked_list(values):
        if not values:
            return None
        head = ListNode(values[0])
        current = head
        for value in values[1:]:
            current.next = ListNode(value)
            current = current.next
        return head

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        node = head.next
        prev = head
        while prev:
            prev.next = node.next
            node.next = prev
            if prev == head:
                head = node
            if prev and prev.next:
                node = prev.next.next
            prev = prev.next
        return head

def printll(ll):
    temp = ll
    while temp:
        print(temp.val, end=', ')
        temp = temp.next

if __name__ == "__main__":
    # The provided lists
    list1 = [1,2,3,4]

    # Build the linked lists
    l1 = ListNode.build_linked_list(list1)

    sol = Solution()
    ll = sol.swapPairs(l1)
    printll(ll)