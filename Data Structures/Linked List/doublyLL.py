class Node:
    def __init__(self, value: int=None):
        # self.value: int = value
        self.value = value
        self.next = None
        self.prev = None
        self.id = hex(id(self))

    # def __dict__(self):
    #     return {}

    
    def __repr__(self):
        return "[" + str(hex(id(self))) + "], " + str(self.value)

    
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            # if node:
            #     prevNode = node.prev
            #     print(prevNode.value)        


    def createDoublyLL(self, nodeValue)->str:
        newNode = Node(nodeValue)
        newNode.next = None
        newNode.prev = None
        self.head = newNode
        self.tail = newNode
        self.length += 1
        return "The DLL is created Successfully"

    def insertNode(self, nodeValue, position):
        newNode = Node(nodeValue)
        if self.head is None:
            print("Doubly Linked List is Empty!!")
        elif position == 0:
            newNode.next = self.head
            newNode.prev = None
            self.head.prev = newNode
            self.head = newNode
            self.length += 1
        else:
            if position < self.length:
                tempNode = self.head
                index = 0
                while index < position - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                if tempNode == self.tail:
                    tempNode.next = newNode
                    newNode.prev = tempNode
                    newNode.next = None
                    self.tail = newNode
                else:
                    tempNode.next = newNode
                    newNode.prev = tempNode
                    newNode.next = nextNode
                    nextNode.prev = nextNode
                self.length += 1
            elif position == self.length:
                newNode.next = None
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode
                self.length += 1
            else:
                print("Position is out of range for this node: " + str(nodeValue))
                
        
    def traversalDLL(self):
        if self.head is None:
            return "Your Doubly Linked List Is Empty!!"
        else:
            node = self.head
            while node is not None:
                print(node.value, end=" ")
                node = node.next
        print()
    
    def reverseTraversalDLL(self):
        if self.head is None:
            return "Your Doubly Linked List Is Empty!!"
        else:
            tempNode = self.tail
            while tempNode is not None:
                print(tempNode.value, end = " ")
                tempNode = tempNode.prev
        print()


    def searchElement(self, nodeValue):
        if self.head is None:
            return "Empty Linked List!!"
        else:
            tempNode = self.head
            while tempNode is not None:
                if tempNode.value == nodeValue:
                    return "Element is present in the linked list!!"
                tempNode = tempNode.next
            return "The node does not exist in this list"
    
    def deleteNode(self, location):
        if self.head is None:
            return "Empty Linked List!!"
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                    self.length -= 1
                else:
                    self.head = self.head.next 
                    self.head.prev = None
                    self.length -= 1
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                if tempNode.next.next is None:
                    tempNode.next = tempNode.next.next
                    self.tail = tempNode
                else:
                    tempNode.next = tempNode.next.next
                    tempNode.next.prev = tempNode
    
    def deleteEntireDLL(self):
        if self.head is None:
            return "Linked List Is Already Empty!!"
        else:
            tempNode = self.head
            while tempNode:
                store = tempNode.next
                del tempNode.value
                tempNode = store
            self.head = None
            self.tail = None
            print("The DLL has been successfully deleted")
                

            



# l1 = 9->1->0
# l2 = 9->0
# l3 = 18 X
# 910
#  90
# -----
# 1000

# stack1 = [0,1,9]
# stack2 = [0,9]
# sum = 0
# carry = 0

# l3 = 0->0
# sum = 0
# carry = 1

# l3 = 0->0->0
# sum = 0
# carry = 1

# l3 = 1->0->0->0

        

        

obj = DoublyLinkedList()
obj.createDoublyLL(0)
obj.insertNode(1,1)
obj.insertNode(2,2)
obj.insertNode(3,3)
obj.insertNode(4,4)
obj.insertNode(5,5)
# obj.traversalDLL()
# obj.reverseTraversalDLL()
# obj.deleteEntireDLL()
# print(obj.traversalDLL())

# print(obj.searchElement(6))
print([node.__dict__ for node in obj])
# print([node.value for node in obj])
