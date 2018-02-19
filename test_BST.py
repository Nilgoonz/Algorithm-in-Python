import BinarySearchTree
import Node

import Test4BST

root = Node.Node(10,4)
G = BinarySearchTree.BinarySearchTree(root)

N1 = Node.Node(12,1)
#N2 = Node.Node(13,2)
#N3 = Node.Node(6,5)
#N4 = Node.Node(4,3)

G.put(N1,root)
#G.put(N2,root)
#G.put(N3,root)
#G.put(N4,root)

G.get(6,root)


test = Test4BST.testBST(G,root)

print test.check(root)

