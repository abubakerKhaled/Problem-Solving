## PROBLEM URL: https://leetcode.com/problems/middle-of-the-linked-list/

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


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class SolutionOne:
    def middleNode(self, head: ListNode) -> ListNode:
        if head.next == None:
            return head
        length = 1
        node = head
        while node:
            length += 1
            node = node.next
        if length %2 == 1:
            middle_indx = int(length / 2 + 1)
        else:
            middle_indx = length / 2
        indx = 1
        node = head
        while node:
            if indx == middle_indx:
                return node
            indx += 1
            node = node.next
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class SolutionTwo:
    def middleNode(self, head: ListNode) -> ListNode:
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow
        

def printll(ll):
    temp = ll
    while temp:
        print(temp.val, end=', ')
        temp = temp.next

if __name__ == "__main__":
    # The provided lists
    list1 = [1,2,3,4,5,6]

    # Build the linked lists
    l1 = ListNode.build_linked_list(list1)

    sol = SolutionOne()
    ll = sol.middleNode(l1)
    printll(ll)

    print()

    sol = SolutionTwo()
    ll = sol.middleNode(l1)
    printll(ll)