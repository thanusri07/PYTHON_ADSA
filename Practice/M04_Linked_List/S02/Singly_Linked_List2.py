'''
Singly Linked List:
Algorithm:
 1.Create Node
 2.Insert the data into the nodes
 3.Generate the Connection btw the nodes
 4.Traverse all the nodes
'''
#By applying singly linked list algorithm:
'''
#1.Create Node
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
#2.Insert the data into the nodes
node1 = Node(15)
node2 = Node(30)
node3 = Node(45)
node4 = Node(60)
#3.Generate the Connection btw the nodes
node1.next = node2
node2.next = node3
node3.next = node4
#4.Traverse all the nodes
def traverse():
    curr=node1
    while curr:
        print(curr.data,end=" ->")
        curr=curr.next
    print("None")
traverse()

 #Operations:
 # 1.Insertion:3 ways
            #  a) Insertion at the beginning 
             # b) Insertion at the end
              # c) Insertion at the specified node
#2.Deletion
'''
#  a) Deletion at the beginning
'''

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
def insert_begin(head,data):
    new_node = Node(data)
    new_node.next = head
    return new_node
def traverse(head):
    curr=head
    while curr:
        print(curr.data,end=" ->")
        curr=curr.next
    print("None")
head=None
head=insert_begin(head,10)
head=insert_begin(head,20)
head=insert_begin(head,30)
print("Insertion at the begin")
traverse(head)

#b.Insertion at the end
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
def insert_begin(head,data):
    new_node = Node(data)
    new_node.next = head
    return new_node
def insert_end(head,data):
    new_node=Node(data)
    if head is None:
        return new_node
    curr=head
    while curr.next:
        curr=curr.next
    curr.next = new_node
    return head
def traverse(head):
    curr=head
    while curr:
        print(curr.data,end=" ->")
        curr=curr.next
    print("None")
head=None
head=insert_begin(head,10)
head=insert_begin(head,20)
head=insert_begin(head,30)
print("Insertion at the begin")
traverse(head)
print()
print("Insertion at the end")
head=insert_end(head,400)
traverse(head)

'''
'''
#c insertion at the specified node
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
def insert_begin(head,data):
    new_node = Node(data)
    new_node.next = head
    return new_node
def insert_end(head,data):
    new_node=Node(data)
    if head is None:
        return new_node
    curr=head
    while curr.next:
        curr=curr.next
    curr.next = new_node
    return head
def insert_at_pos(node, data):
    if node is None:
        print("Error")
        return 
    new_node = Node(data)
    new_node.next = node.next
    node.next = new_node
def traverse(head):
    curr=head
    while curr:
        print(curr.data,end=" ->")
        curr=curr.next
    print("None")
head=None
head=insert_begin(head,10)
head=insert_begin(head,20)
head=insert_begin(head,30)
print("Insertion at the begin")
traverse(head)
print()
print("Insertion at the end")
head=insert_end(head,400)
traverse(head)
print("Insertion at the specified node")
insert_at_pos(head, 25)
traverse(head)
Deletion: 3 ways
   a) Deletion at the beginning
   b) Deletion at the end
   c) Deletion at the specified node
'''
#a) Deletion at the beginning
'''
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
def insert_begin(head,data):
    new_node = Node(data)
    new_node.next = head
    return new_node
def deletion_begin(head):
    if head is None:
        print("Error")
        return None
    new_head= head.next
    del head
    return new_head
def traverse(head):
    curr=head
    while curr:
        print(curr.data,end=" ->")
        curr=curr.next
    print("None")
head=None
head=insert_begin(head,10)
head=insert_begin(head,20)
head=insert_begin(head,30)
print("Insertion at the begin")
traverse(head)
print()
print("Deletion at the begin")
head=deletion_begin(head)
traverse(head)
print()

#b) Deletion at the end
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
def insert_begin(head,data):
    new_node = Node(data)
    new_node.next = head
    return new_node
def insert_end(head,data):
    new_node=Node(data)
    if head is None:
        return new_node
    curr=head
    while curr.next:
        curr=curr.next
    curr.next = new_node
    return head
def deletion_end(head):
    if head is None or head.next is None:
        print("Error")
        return None
    curr=head
    while curr.next.next:
        curr=curr.next
    del_node = curr.next
    curr.next=None
    del del_node
def insert_at_pos(node, data):
    if node is None:
        print("Error")
        return 
    new_node = Node(data)
    new_node.next = node.next
    node.next = new_node
def traverse(head):
    curr=head
    while curr:
        print(curr.data,end=" ->")
        curr=curr.next
    print("None")
head=None
head=insert_begin(head,10)
head=insert_begin(head,20)
head=insert_begin(head,30)
print("Insertion at the begin")
traverse(head)
print()
print("Insertion at the end")
head=insert_end(head,400)
traverse(head)
print()
print("Deletion at the end")
head=deletion_end(head)
traverse(head)
print()
''' 
#c) Deletion at the specified node
'''
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
def insert_begin(head,data):
    new_node = Node(data)
    new_node.next = head
    return new_node
def insert_end(head,data):
    new_node=Node(data)
    if head is None:
        return new_node
    curr=head
    while curr.next:
        curr=curr.next
    curr.next = new_node
    return head
def insert_at_pos(node, data):
    if node is None:
        print("Error")
        return 
    new_node = Node(data)
    new_node.next = node.next
    node.next = new_node
def deletion_at_pos(node):
    if node is None or node.next is None:
        print("Error")
        return
    new_node=node.next
    node.next=new_node.next
    del new_node
def traverse(head):
    curr=head
    while curr:
        print(curr.data,end=" ->")
        curr=curr.next
    print("None")
head=None
head=insert_begin(head,10)
head=insert_begin(head,20)
head=insert_begin(head,30)
print("Insertion at the begin")
traverse(head)
print()
print("Insertion at the end")
head=insert_end(head,400)
traverse(head)
print("Insertion at the specified node")
insert_at_pos(head, 25)
traverse(head)
print("Deletion at the specified node")
deletion_at_pos(head)
traverse(head)
print()
'''