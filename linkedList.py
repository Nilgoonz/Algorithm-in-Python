

import NodeLinkedList

class linkedList:

    def __init__(self):

        self.head=None
        self.tail=None


    def push(self,Node):

        if self.head == None:
            self.head = Node
            Node.tail = Node
            Node.previous = None
            Node.nextNode = None

        else:
            self.head.previous = Node
            Node.nextNode = self.head
            Node.previous = None
            self.head = Node


