
import SearchLoop
import NodeLinkedList
import linkedList


def checkloop( L1):
    if L1.head.nextNode == None:
        return True

    Newhead1 = L1.head
    print Newhead1.value
    Newhead2 = L1.head

    while (Newhead1 is not None and Newhead2 is not None):

        Newhead1 = Newhead1.nextNode
        print Newhead1.value
        Newhead2 = Newhead2.nextNode.nextNode

        if Newhead1 == Newhead2:
            return False
    return True


N1 = NodeLinkedList.Node(1)
N2 = NodeLinkedList.Node(2)
N3 = NodeLinkedList.Node(3)
N4 = NodeLinkedList.Node(4)
N5 = NodeLinkedList.Node(5)
N6 = NodeLinkedList.Node(6)

L1 = linkedList.linkedList()
L1.push(N1)
L1.push(N2)
L1.push(N3)
L1.push(N4)
L1.push(N5)
L1.push(N6)



N3.nextNode = N6

# L1.push(N2)

print checkloop(L1)

