import json
from re import template

class NodeJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        return str(obj)


class Node:
    
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None
        self.id = str(hex(id(self)))

    def __str__(self):
        return str(hex(id(self)))

    def __repr__(self):
        return "[" + str(hex(id(self))) + "], " + str(self.value)


class circularDoublyLL:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break
    
    def createCircularDoublyLL(self, nodeValue):
        firstNode = Node(nodeValue)
        self.head = firstNode
        self.tail = firstNode
        firstNode.next = self.head
        firstNode.prev = self.tail
        self.length += 1
        return "Your Circular Doubly LL has been created!!"
    
    def insertNode(self, nodeValue, location):
        if self.head is None:
            print("Your circular doubly LL is Empty!!")
        else:
            newNode = Node(nodeValue)
            if location == 0:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.head = newNode
                self.tail.next = newNode                
                self.length += 1
            else:
                if location <= self.length:
                    tempNode = self.head
                    index = 0
                    while index < location - 1:
                        tempNode = tempNode.next
                        index += 1
                    nextNode = tempNode.next
                    if tempNode == self.tail:
                        tempNode.next = newNode
                        newNode.prev = tempNode
                        newNode.next = self.head
                        self.head.prev = newNode
                        self.tail = newNode
                    else:
                        tempNode.next = newNode
                        newNode.prev = tempNode
                        newNode.next = nextNode
                        nextNode.prev = nextNode
                    self.length += 1
    
    def traversalCDLL(self):
        node = self.head
        while node:
            print(node.value, end=" ")
            node = node.next
            if self.head == node:
                break
        print()

    def searchNodeCDLL(self, nodeValue):
        if self.head is None:
            print("Your circular doubly LL is Empty!!")
        else:
            tempNode = self.head
            index = 0
            while index < self.length:
                if nodeValue == tempNode.value:
                    return "Node is present in CDLL at location: " + str(index)
                tempNode = tempNode.next
                index += 1
        return "Node is not present in CDLL"

    def deleteNode(self, position):
        if self.head is None:
            print("Your circular doubly LL is Empty!!")
        else:
            if position == 0:
                self.head = self.head.next
                self.head.prev = self.tail
                # print(self.head.value)
                self.length -= 1
            else:
                if position < self.length:
                    tempNode = self.head
                    index = 0
                    while index < position - 1:
                        tempNode = tempNode.next
                        index += 1
                    if tempNode.next == self.tail:
                        tempNode.next = self.head
                        self.head.prev = tempNode
                        self.tail = tempNode
                    else:
                        tempNode.next = tempNode.next.next
                        tempNode.next.prev = tempNode
                    self.length -= 1
                else:
                    print("Node Position Out Of Range!!")
                        

    def deleteEntireCDLL(self):
        if self.head is None:
            print("Your circular doubly LL is Empty!!")
        else:
            tempNode = self.head
            while tempNode:
                store = tempNode.next
                del tempNode.value
                tempNode.next = None
                # print(tempNode.next)
                tempNode = store
                if tempNode == self.head:
                    break
            self.head = None
            self.tail = None
                





        

                
                

                    


obj = circularDoublyLL()
obj.createCircularDoublyLL(4)
obj.insertNode(3,0)
obj.insertNode(2,0)
obj.insertNode(1,0)
obj.insertNode(5,4)
obj.traversalCDLL()
# print(obj.searchNodeCDLL(6))
obj.deleteEntireCDLL()

# print([node.value for node in obj])
data = [node.__dict__ for node in obj]
# result = NodeJSONEncoder().encode(data)
result = json.dumps(json.loads(NodeJSONEncoder().encode(data)),indent=4)
print(result)

