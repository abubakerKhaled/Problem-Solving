from copy import deepcopy


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
            while node and head:
                if node.val != head.val:
                    return False
                node = node.next
                head = head.next
            
            return True



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
    ll = sol.isPalindrome(l1)
    printll(ll)