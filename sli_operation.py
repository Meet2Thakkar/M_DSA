class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtB(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insertAfter(self,prev_node, data):
        m = self.head
        while m is not None:
            if prev_node == m.data:
                break
            m = m.next
        
        if m is None:
            print("The given previous node must be in LS")
        else:    
            new_node = Node(data)
            new_node.next = m.next
            m.next = new_node

    def insertBefore(self, x, data):
        if self.head.data == x:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            return
            
        n = self.head
        while n.next is not None:
            if n.next.data == x:
                break
            n = n.next
        if n.next is None:
            print("Node not found")
        else:
            new_node = Node(data)
            new_node.next = n.next
            n.next = new_node

    def insertAtE(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next is not None:
            last = last.next
        last.next = new_node

    def insert_empty(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("Linked list is not empty")

    def delete_begin(self):
        if self.head is None:
            print("LL is empty")
        else:
            self.head = self.head.next

    def delete_end(self):
        if self.head is None:
            print("LL is empty")
        elif self.head.next is None:
            self.head = None
        else:
            n = self.head
            while n.next.next is not None:
                n = n.next
            n.next = None

    def delete_by_value(self, x):
        if self.head is None:
            print("can't delete empty LL")
            return
        if x == self.head.data:
            self.head = self.head.next
            return
        n = self.head
        while n.next is not None:
            if x == n.next.data:
                break
            n = n.next
        if n.next is None:
            print("Node not found")
        else:
            n.next = n.next.next

    def search(self, x):
        if self.head is None:
            print("can't find in empty LL")
            return
        n = self.head
        while n is not None:
            if x == n.data:
                return True
            n = n.next
            return False
    
    def printLL(self):
        temp = self.head
        while (temp):
            print(str(temp.data) + " -->", end=" ")
            temp = temp.next

llist = LinkedList()
llist.insertAtB(1)
llist.insertAtB(0)
llist.insertAtE(2)
llist.insertAtE(4)
llist.insertAfter(2, 3)
llist.insertBefore(4, 3.5)
llist.insertBefore(0, -1)
llist.insert_empty(10)

print("Linked list: ")
llist.printLL()

print("\nAfter deleting an element:")
llist.delete_begin()
llist.delete_end()
llist.delete_by_value(3)
llist.printLL()

print("\nSearching Node: ")
llist.search(3)