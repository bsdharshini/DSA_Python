class NewNode:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value):
        newNode = NewNode(value)
        self.head = newNode
        self.tail = newNode
        self.length = 1
    
    def append(self,value):
        newNode = NewNode(value)
        if(self.head is None and self.tail is None):
            self.head,self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.length+= 1
        print ("Added element %d at the end"%(value))
    
    def pop(self):
        if(self.head is None and self.tail is None):# or self.length == 0
            print("No node to delete")
        else:
            temp = self.head
            pre = self.head
            while temp.next:
                pre = temp
                temp = temp.next
            self.tail = pre
            self.tail.next = None
            self.length -=1
            if(self.length == 0):
                self.tail = None
                self.head = None
            print ("Popped element %d at end"%(temp.value))
    
    
    def prepend(self,value):
        newNode = NewNode(value)
        if(self.head is None and self.tail is None):
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode 
        self.length +=1
        print("Added first element %d"%(value))
    
    def popFirst(self):
        if(self.length == 0):
            print("No element to pop")
        else:
            temp = self.head
            self.head = temp.next
            temp.next = None
            self.length -=1
            if(self.length == 0):
                self.tail = None
            print("Popped element %d at first"%(temp.value))
            
    def insertAtIndex(self,value,index):
        newNode = NewNode(value)
        temp = self.head
        if(index<0 or index >=self.length):
            print("Index out of bound")
        i = 0
        if(self.length == 0):
            self.head = newNode
            self.tail = newNode
        else:
            while temp.next:
                if i == index:
                    nextEle = temp.next
                    newNode.next = nextEle
                    temp.next = newNode
                    break
                i+=1
        self.length += 1
        print("Added element %d at index %d"%(value,index))
        
    def popAtIndex(self,index):
        if(self.length == 0):
            print("No element to delete")
        else:
            temp = self.head
            for _ in range(index):
                pre = temp
                temp = temp.next
            pre.next = temp.next
            self.length -=1
            print("Popped element %d at index %d"%(temp.value,index))
            
    def getValue(self,index): # search 
        temp = self.head
        for i in range(index):
            temp = temp.next
        print("The value at %d is %d"%(index,temp.value))
            
    
    def printLL(self):
        temp = self.head
        i= 0
        while temp is not None:
            print('Element %d is: %d'%(i,temp.value))
            temp=temp.next
            i+=1
            
ll = LinkedList(3)
ll.append(4)
ll.append(9)
ll.append(11)
ll.pop()
ll.prepend(5)
ll.popFirst()
ll.insertAtIndex(8,1)
ll.getValue(2)
ll.popAtIndex(2)
ll.printLL()
