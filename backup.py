# use linked list to add two values

import linkedList


class addTwo:
    linkedList = linkedList.linkedList()

    def __init__(self, a, b):

        self.firstNum = a
        self.secondNum = b
        self.list = []
        tail1 = self.firstNum.tail
        tail2 = self.secondNum.tail
        self.addtwo(tail1, tail2)

    def addtwo(self, tail1, tail2):
        carry = 0
        list = []

        while tail1 != None and tail2 != None:

            if tail1 == None:
                tailValue1 = 0

            sum = tail1.value + tail2.value + carry
            carry = sum / 10
            currentValue = sum % 10
            self.list.insert(0, currentValue)
            tail1 = tail1.previous
            tail2 = tail2.previous
        if carry > 0:
            self.list.insert(0, 1)

