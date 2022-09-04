class Node:
    def __init__(self, data):
        self.data = data
        self.nref = None
        self.pref = None            

class doublyLL:
    def __init__(self):
        self.head = None

    def print_ll(self):
        if self.head is None:
            print("Linked is empty!")
        else:
            n = self.head
            while n is not None:
                print(n.data, "-->",end=" ")
                n = n.nref

    def print_ll_reverse(self):
        print()
        if self.head is None:
            print("Linked is empty!")
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            while n is not None:
                print(n.data, "<--", end=" ")
                n = n.pref

    def insert_empty(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("Linked List is not empty!!")

    def add_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
    
        else:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.nref = new_node
            new_node.pref = n    

    def add_after(self, data, x):
        if self.head is None:
            print("Empty LL!!")
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.nref
            if n is None:
                print("X is not present in DLL")
            else:
                new_node = Node(data)
                new_node.nref = n.nref
                new_node.pref = n
                if n.nref is not None:
                    n.nref.pref = new_node
                n.nref = new_node
    def add_before(self, data, x):
        if self.head is None:
            print("Empty LL!!")
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.nref
            if n is None:
                print("X is not present in DLL")
            else:
                new_node = Node(data)
                new_node.nref = n
                new_node.pref = n.pref
                if n.pref is not None:
                    n.pref.nref = new_node
                else:
                    self.head = new_node
                n.pref = new_node

    def delete_begin(self):
        if self.head is None:
            print("DLL is empty!")
            return
        if self.head.nref is None:
            self.head = None
            print("DLL is empty after deleting node")
        else:
            self.head = self.head.nref
            self.head.pref = None
    def delete_end(self):
        if self.head is None:
            print("DLL is empty!")
            return
        if self.head.nref is None:
            self.head = None
            print("DLL is empty after deleting node")
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.pref.nref = None
    
    def delete_value(self, x):
        if self.head is None:
            print("DLL is empty!")
            return
        if self.head.nref is None:
            if x == self.head.data:
                self.head = None
                print("DLL is empty after deleting node")
            else:
                print("x is not in DLL")
            return
        if x == self.head.data:
            self.head = self.head.nref
            self.head.pref = None
            return
        n = self.head.nref
        while n.nref is not None:
            if x == n.data:
                break
            n = n.nref
        if n.nref is not None:
            n.pref.nref = n.nref
            n.nref.pref = n.pref
        else:
            if n.data == x:
                n.pref.nref = None
            else:
                print("x not found") 




dl1 = doublyLL()
#dl1.insert_empty(10)
#dl1.insert_empty(20)
dl1.add_begin(0)
dl1.add_begin(10)
dl1.add_end(20)
dl1.add_end(30)
dl1.add_after(25,20)
dl1.add_before(5,10)
dl1.add_after(40,30)
dl1.delete_begin()
dl1.delete_end()
dl1.delete_value(20)
dl1.delete_value(10)
dl1.delete_value(30)
dl1.print_ll()
dl1.print_ll_reverse()