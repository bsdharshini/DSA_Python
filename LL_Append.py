class Node:
    # creating new node is a common function for all append/ insert/ prepend methods

    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:

    def __init__(self,value):
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        self.length = 1

    def append(self,value):
        newNode = Node(value)
        if(self.head is None and self.tail is None): # if list is empty
            self.head = newNode
            self.tail = newNode
        else: 
            self.tail.next = newNode # add node to the list
            self.tail = newNode # move the tail to next node
        self.length+=1 # update the length
        return True 

    def printLL(self):
        temp = self.head
        i= 1
        while temp is not None:
            print('Element %d is: %d'%(i,temp.value))
            temp=temp.next
            i+=1
            


myLinked = LinkedList(7)
myLinked.append(4)
myLinked.append(6)
myLinked.printLL()
print('Length',myLinked.length)
