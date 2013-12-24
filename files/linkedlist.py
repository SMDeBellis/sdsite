#!/usr/bin/python3

class node:
    
    def __init__(self):
        self.nextNode = None
        self.data = 0

    def setNextNode(self, toPointTo):
        self.nextNode  = toPointTo

    def getNextNode(self):
        return self.nextNode

    def setNodeData(self, toSet):
        self.data = toSet

    def getNodeData(self):
        return self.data

class ll:
    
    def __init__(self):
        self.head = None

    def insert(self, toInsert):
        
        if toInsert == None:
            return 1

        elif self.head == None:
            self.head = node()
            self.head.setNodeData(toInsert)

        else:

            current = self.head

            while current.getNextNode() != None:
                current = current.getNextNode()

            temp = node()
            temp.setNodeData(toInsert)
            current.setNextNode(temp)

        return 0
 
    def remove(self, toRemove):

        current = self.head
        
        while current != None and current.getNodeData() != toRemove:
            previous = current
            current = current.getNextNode()

        if current == None:
            return None
        else:
            previous.setNextNode(current.getNextNode())

    def printList(self):
        
        if self.head == None:
            return 1

        else:
            iterator = self.head
    
            while iterator != None:
                print(iterator.getNodeData())
                iterator = iterator.getNextNode()
        
        return 0

    def destroyList(self):
        self.head = None

if __name__ == '__main__':
    
    """
    MyList = ll()
    MyList.insert(4)
    MyList.insert(3)
    MyList.insert(45)
    MyList.insert("fish")
    MyList.insert("pickle")
    MyList.printList()
    MyList.remove("fish")
    MyList.printList()
    MyList.destroyList()
    MyList.printList()
    
    test = node()
    test2 = node()
    test.setNodeData("fish")
    test2.setNodeData("pizza")
    test.setNextNode(test2)
    print(test.getNextNode().getNodeData())
    """

