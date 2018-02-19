

# this class test to see whether a given tree is binary search tree or not


import Node
import BinarySearchTree

class testBST:

    def __init__(self,tree,root):

        self.root = root
        self.tree = tree

    def check(self,Root):

        while Root != None:

            leftNode= Root.left
            rightNode = Root.right
            if leftNode is None and rightNode is None:
                return True
            leftGood = leftNode is None
            rightGood = rightNode is None
            if leftNode != None and Root.key > leftNode.key:
                NewRoot = Root.left
                leftGood=self.check(NewRoot)

            if rightNode != None and Root.key < rightNode.key:
                NewRoot = Root.right
                rightGood = self.check(NewRoot)

            return leftGood and rightGood





