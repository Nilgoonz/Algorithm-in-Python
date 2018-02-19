# use linked list to add two values

import linkedList

class addTwo:
    linkedList = linkedList.linkedList()
    def __init__(self,a,b):

        self.firstNum = a
        self.secondNum = b
        self.list= []
        tail1 = self.firstNum.tail
        tail2 = self.secondNum.tail
        self.addtwo(tail1,tail2)

    def addtwo(self,tail1,tail2):
        carry = 0
        list = []

        while tail1 != None or tail2 != None:

            if tail1 == None:
                tailValue1 = 0
                tailValue2 = tail2.value
                tail2 = tail2.previous
            if tail2 == None:
                tailValue2 = 0
                tailValue1 = tail1.value
                tail1 = tail1.previous
            else:
                tailValue1 = tail1.value
                tailValue2 = tail2.value
                tail1 = tail1.previous
                tail2 = tail2.previous
            sum = tailValue1 + tailValue2 + carry
            carry = sum/10
            currentValue = sum%10
            self.list.insert(0,currentValue)
        if carry>0:
            self.list.insert(0, 1)

