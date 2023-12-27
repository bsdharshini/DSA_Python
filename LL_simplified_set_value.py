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
    
    def popL(self):
        if(self.length == 0): # we can also use self.tail is None and self.head is None 
            # print("No node to delete")
            return "No node to delete"           
        else:
            # delete element when next is None
            #
            temp = self.head
            pre = self.head
            while temp.next: # or temp is not None
                pre = temp
                temp = temp.next
                
            self.tail = pre
            self.tail.next = None
            self.length-=1
            if(self.length == 0 ): # diff b/w the above self.length == 0 is this will run only if the list has only one node
                self.head = None
                self.tail = None

            return temp.value

    def prepend(self,value):
        temp = self.head
        newNode = Node(value)
        if(self.length == 0):
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = temp
            self.head = newNode
        self.length+=1
        return True
    
    def pop_first(self):
        if(self.length == 0):
            return None
        else:
            temp = self.head
            self.head = temp.next
            temp.next = None
            self.length -=1
            if(self.length == 0):
                self.tail = None
            return temp

    def printLL(self):
        temp = self.head
        i= 1
        while temp is not None:
            print('Element %d is: %d'%(i,temp.value))
            temp=temp.next
            i+=1

    def getValue(self,index):
        temp = self.head
        if(index < 0 and index >= self.length):
            return None
        for _ in range(index):
            temp = temp.next
        return temp.value
    
    def setValue(self,index,value):
        temp = self.head
        if(index < 0 and index >= self.length):
            return None
        for _ in range(index):
            temp = temp.next
        temp.value = value
        return temp.value
    
    def simplifiedSetValue(self,index,value):
        temp = self.getValue(index) # this will get the index node
        temp.value = value 



myLinked = LinkedList(7)
myLinked.append(4)
myLinked.append(6)


print(myLinked.prepend(10))
myLinked.printLL()
print('Length',myLinked.length)
print(myLinked.pop_first())
myLinked.printLL()
print(myLinked.getValue(2))
print(myLinked.setValue(2,1))
print(myLinked.simplifiedSetValue(1,8))
myLinked.printLL()
