class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class MyHashSet:
    def __init__(self):
        self.dummy = Node(0)  # Dummy head
        self.tail = self.dummy  # Keep track of the last node

    def add(self, key: int) -> None:
        curr = self.dummy
        while curr.next:
            if curr.next.val == key:
                return  # Key already exists
            curr = curr.next
        curr.next = Node(key)
        self.tail = curr.next

    def remove(self, key: int) -> None:
        curr = self.dummy
        while curr.next:
            if curr.next.val == key:
                curr.next = curr.next.next
                if curr.next is None:
                    self.tail = curr  # Update tail if last element is removed
                return
            curr = curr.next

    def contains(self, key: int) -> bool:
        curr = self.dummy.next
        while curr:
            if curr.val == key:
                return True
            curr = curr.next
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)



def printll(ll):
    temp = ll
    while temp:
        print(temp.val, end=', ')
        temp = temp.next

if __name__ == "__main__":
    keys = [1, 2, 3, 4, 5]
    obj = MyHashSet()
    for key in keys:
        obj.add(key)
    obj.remove(key)
    param_3 = obj.contains(key)