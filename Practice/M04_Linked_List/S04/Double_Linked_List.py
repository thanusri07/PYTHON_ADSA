#Deletion at beginning
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class Double_LL:
    def __init__(self):
        self.head = None
    def insert_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head=new_node
    def insert_end(self,data):
        new_node=Node(data)
        if self.head==None:
            return new_node
        curr=self.head
        while curr.next:
            curr=curr.next
        curr.next=new_node
        new_node.prev=curr
    def deletion_begin(self):
        if self.head is None:
            print("Error")
            return None
        new_head=self.head
        self.head=self.head.next
        del new_head
    def deletion_end(self):
        if self.head is None:
            print("Error")
            return None
         
    def traverse(self):
        curr=self.head
        while curr:
            print(curr.data,end="<->")
            curr=curr.next
        print("None")
dll=Double_LL()
dll.insert_begin(10)
dll.insert_begin(20)
dll.insert_begin(30)
dll.traverse()
dll.insert_end(40)
dll.insert_end(50)
dll.traverse()
dll.deletion_begin()
dll.traverse()