class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def insert_at_end(head, data):
        # Insert a new node with given data at the end of the linked list
        new_node = ListNode(data)
        if head is None:
            return new_node

        current = head
        while current.next:
            current = current.next

        current.next = new_node
        return head


from copy import deepcopy
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # if 1 element return True
        # else generate another list and reverse the old list
        # trace the two lists
        # if they are equal return True
        # else return False
        if not head.next:
            return True
        else:
            node = deepcopy(head)
            prev = None
            while node:
                next = node.next
                node.next = prev
                prev = node
                node = next
            while prev and head:
                if prev.val != head.val:
                    return False
                prev = prev.next
                head = head.next
            
            return True



def printll(ll):
    temp = ll
    while temp:
        print(temp.val, end=', ')
        temp = temp.next

if __name__ == "__main__":
    head = [1,2,2,1]
    ln = ListNode(val=1)
    for i in head[1:]:
        ln.insert_at_end(i)
    sol = Solution()
    res = sol.isPalindrome(ln)
    print(res)