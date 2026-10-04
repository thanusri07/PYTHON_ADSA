'''
Queue->First In First Out
insert an element->enqueue using rear pointer(end)
deletion an element->dequeue using front pointer
Built in methods:
1.enqueue->append()
2.dequeue->pop(0)  0 elememt delete
3.peek(front element from queue)->q[0]
4.is_empty()->len(q)==0
5.size()->
'''
#Queue implementation using List
class Queue(self):
    def __init__(self):
        self.q=[]
    def Enqueue(self,val):
        self.q.append(val)
    def Dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        return self.q.pop(0)
    def is_empty(self):
        return len(self.q)==0
    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        return self.q[0]
qu=Queue()
qu.enqueue(100)
qu.enqueue(200)
qu.enqueue(300)



