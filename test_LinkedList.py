
import NodeLinkedList

import linkedList

import addTwoValue


N1 = NodeLinkedList.Node(4)
N2 = NodeLinkedList.Node(3)
N3 = NodeLinkedList.Node(2)
L1 = linkedList.linkedList()
L1.push(N1)
print L1.tail
L1.push(N2)
L1.push(N3)

M1 = NodeLinkedList.Node(3)
M2 = NodeLinkedList.Node(6)
#M3 = NodeLinkedList.Node(5)

L2 = linkedList.linkedList()
L2.push(M1)
L2.push(M2)
#L2.push(M3)


addtwo = addTwoValue.addTwo(L1,L2)


print addtwo.list
