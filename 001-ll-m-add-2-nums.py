# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        num1 = 0
        num2 = 0
        while l1:
            num1 = num1 * 10 + l1.val
            l1 = l1.next
        while l2:
            num2 = num2 * 10 + l2.val
            l2 = l2.next
        num1 = str(num1)
        num1 = num1[::-1]
        num1 = int(num1)
        num2 = str(num2)
        num2 = num2[::-1]
        num2 = int(num2)
        num = num1 + num2
        num = str(num)
        num = num[::-1]
        l = ListNode(num[0])
        dumy = l
        for i in range(1, len(num)):
            ll = ListNode(num[i])
            dumy.next = ll
            dumy = dumy.next
        return l
    
def printll(ll):
    temp = ll
    while temp:
        print(temp.val, end=', ')
        temp = temp.next

if __name__ == "__main__":
    # The provided lists
    list1 = [0, 8, 6, 5, 6, 8, 3, 5, 7]
    list2 = [6, 7, 8, 0, 8, 5, 8, 9, 7]

    # Build the linked lists
    l1 = ListNode.build_linked_list(list1)
    l2 = ListNode.build_linked_list(list2)

    sol = Solution()
    ll = sol.addTwoNumbers(l1, l2)
    printll(ll)