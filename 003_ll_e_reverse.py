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
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        else:
            curr, prev = head, None
            while curr:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
            return prev

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
    ll = sol.reverseList(l1)
    printll(ll)