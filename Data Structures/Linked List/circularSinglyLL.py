class Node:

    # init method or constructor  
    def __init__(self, value=None):
        self.value = value
        self.next = None
    
class circularSinglyLL:

    # init method or constructor  
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            print(node.value)
            node = node.next
            if node == self.tail.next:
                break
            
    
    def createCSLL(self, nodeValue):
        firstNode = Node(nodeValue)
        firstNode.next = firstNode
        self.head = firstNode
        self.tail = firstNode
        self.length += 1
        return "Your Circular Singly LL has been created!!"

    #  Insertion of a node in circular singly linked list
    def insertNode(self, nodeValue, location):
        if self.head is None:
            print("Circular Singly Linked List Is Empty!!")
        else:
            newNode = Node(nodeValue)
            # print(self.length)
            if location == 0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode
                self.length += 1
            elif location >= self.length:
                newNode.next = self.tail.next
                self.tail.next = newNode
                self.tail = newNode
                self.length += 1
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
                self.length += 1
        return "The node has been successfully inserted"
    
    # Traversal of a node in circular singly linked list
    def traversalNode(self):
        if self.head is None:
            print("Circular Singly Linked List Is Empty!!")
        else:
            node = self.head
            while node:
                print(node.value, end=" ")
                node = node.next
                if node == self.tail.next:
                    break
            print()
        # print(self.length)


    # Searching for a node in circular singly linked list
    def searchNode(self, nodeValue):
        if self.head is None:
            print("Circular Singly Linked List Is Empty!!")
        else:
            toFind = self.head
            # index = 0
            # while index < self.length:
            #     if toFind.value == nodeValue:
            #         return "Node Found: " + str(toFind.value)
            #     index += 1
            #     toFind = toFind.next
            # return "Node does not exist in the circular singly linked list!!"

            while toFind:
                if toFind.value == nodeValue:
                    return "Node Found: " + str(toFind.value)
                toFind = toFind.next
                if toFind.next == self.tail.next:
                    return "Node does not exist in the circular singly linked list!!"

    #1 -> 2 -> 3 -> 4 -> 5 ->(1)

    def deleteNode(self, location):
        if self.head is None:
            print("Circular Singly Linked List Is Empty!!")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                    self.length -= 1
                else:
                    self.head = self.head.next
                    self.tail.next = self.head
                    self.length -= 1
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next
                self.length -= 1



    def deleteEntireCSLL(self):
        if self.head is None:
            return "Singly Linked List Is Already Empty!!"
        else:
            self.head = None
            self.tail.next = None
            self.tail = None


obj = circularSinglyLL()
obj.createCSLL(1)
obj.insertNode(2, 1)
obj.insertNode(3, 2)
obj.insertNode(4,3)
obj.insertNode(5, 1)
obj.insertNode(6, 5)
obj.traversalNode()
# print(obj.searchNode(1))
obj.deleteNode(2)
obj.traversalNode()
obj.deleteEntireCSLL()
obj.traversalNode()
print([node.value for node in obj])
