class Node:
    def __init__(self, key, value, next=None):
        self.key = key
        self.value = value
        self.next = next


class MyHashMap:

    def __init__(self):
        self.array = [0] * 1000


    def put(self, key: int, value: int) -> None:
        indx = self.hash_function(key)
        if self.array[indx] == 0:
            node = Node(key, value)
            self.array[indx] = node
        else:
            node = self.array[indx]
            while node.next:
                if node.key == key:
                    node.value = value
                    return 
                node = node.next
            if node.key == key:
                node.value = value
                return 
            else:
                new_node = Node(key, value)
                node.next = new_node

    def get(self, key: int) -> int:
        indx = self.hash_function(key)
        node = self.array[indx]
        while node:
            if node.key == key:
                return node.value
            node = node.next
        return -1

    def remove(self, key: int) -> None:
        indx = self.hash_function(key)
        node = self.array[indx]
        prev = None
        while node:
            if node.key == key and prev == None:
                if node.next == None:
                    self.array[indx] = 0
                else:
                    self.array[indx] = node.next
            if node.key == key and prev != None:
                prev.next = node.next
            prev = node
            node = node.next

    def hash_function(self, key):
        return key % 1000



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)



def printll(ll):
    temp = ll
    while temp:
        print(temp.val, end=', ')
        temp = temp.next

if __name__ == "__main__":
    keys = [1, 2, 3, 4, 5]
    values = [7, 8, 4, 6, 9]
    obj = MyHashMap()
    for value in values:
        for key in keys:
            obj.put(key, value)
    obj.remove(keys[2])
    param_3 = obj.get(keys[3])
    print(param_3)