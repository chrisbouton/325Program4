#Christopher Bouton and A.....
#Dr. Lori
#Advanced Data Structures 325
#Program 4: Campus Recycling


#data = vertex
class Vertex:
    def __init__(self, data):
        self.data = data
        self.edges = LinkedList()
        self.found = False

    def getData(self):
        return self.data

    def setData(self, data):
        self.data = data
    

class Edge(Vertex):
    def __init__(self, weight, origin=None, dest=None):
        self.origin = origin
        self.dest = dest
        self.weight = weight
       # self.node = Node()
    
    def getOrigin(self):
        return self.origin

    def setOrigin(self, origin):
        self.origin = origin

    def getDest(self):
        return self.dest
    
    def setDest(self, dest):
        self.dest = dest

    ##might not be right
    def getEndPoints(self):
        return self.getOrigin(), self.getDest()

    def opposite(self, vertex):
        if (self.getOrigin() == vertex):
            return self.getDest()
        elif(self.getDest() == vertex):
            return self.getOrigin()
        else: 
            return -1

class Node:
    ##constructor
    def __init__(self):    
        self.childs = LinkedList()
        self.word = False
        self.data = None
        self.next = None
        self.prev = None


# Python program to insert in sorted list 
  
class LinkedList:
    numItems = 0 

    # Function to initialize head 
    def __init__(self): 
        self.head = None
  
    def sortedInsert(self, new_node): 
          
        # Special case for the empty linked list  
        if self.head is None: 
            new_node.next = self.head 
            self.head = new_node 
            self.numItems += 1
        # Special case for head at end 
        elif self.head.data >= new_node.data: 
            new_node.next = self.head 
            self.head = new_node 
            self.numItems += 1
        else : 
  
            # Locate the node before the point of insertion 
            current = self.head 
            while(current.next is not None and current.next.data < new_node.data): 
                current = current.next
              
            new_node.next = current.next
            current.next = new_node 
            self.numItems += 1
    # Function to insert a new node at the beginning 
    def push(self, new_data): 
        new_node = Node()
        new_node.data = new_data 
        new_node.next = self.head 
        self.head = new_node 
        self.numItems += 1
  
    # Utility function to prit the linked LinkedList 
    def printList(self): 
        temp = self.head 
        while(temp): 
            print (temp.data) 
            temp = temp.next
  
  
# # Driver program 
# llist = LinkedList() 
# new_node = Node(5) 
# llist.sortedInsert(new_node) 
# new_node = Node(10) 
# llist.sortedInsert(new_node) 
# new_node = Node(7) 
# llist.sortedInsert(new_node) 
# new_node = Node(3) 
# llist.sortedInsert(new_node) 
# new_node = Node(1) 
# llist.sortedInsert(new_node) 
# new_node = Node(9) 
# llist.sortedInsert(new_node) 
# print "Create Linked List"
# llist.printList() 
    def goTo(self, m):
        
        self.curr = self.head
        i = 0
        while (i < m):
            if(self.curr.next != None):
                self.curr = self.curr.next
                i += 1
            else:
                break
        
        return self.curr

##got queue class from <https://stackoverflow.com/questions/45688871/implementing-an-efficient-queue-in-python>
class QNode(object):
  def __init__(self, item = None):
    self.item = item
    self.next = None
    self.previous = None


class Queue(object):
  def __init__(self):
    self.length = 0
    self.head = None
    self.tail = None

  def enqueue(self, x):
    newNode = QNode(x)
    if self.head == None:
      self.head = self.tail = newNode
    else:
      self.tail.next = newNode
      newNode.previous = self.tail
      self.tail = newNode
    self.length += 1


  def dequeue (self):
    item = self.head.item
    self.head = self.head.next 
    self.length -= 1
    if self.length == 0:
      self.last = None
    return item

##stack class site <https://www.pythoncentral.io/stack-tutorial-python-implementation/>
class Stack:
    
    #Constructor 
    def __init__(self, max_size):
        self.stack = list()
        self.maxSize = max_size
        self.top = 0
    
    #Adds element to the Stack
    def push(self,data):
        if self.top>=self.maxSize:
            return ("Stack Full!")
        self.stack.append(data)
        self.top += 1
        return True
        
    #Removes element from the stack
    def pop(self):
        if self.top<=0:
            return ("Stack Empty!")
        item = self.stack.pop()
        self.top -= 1
        return item
        
    #Size of the stack
    def size(self):
        return self.top

# s = Stack(8)
# print(s.push(1))#prints True
# print(s.push(2))#prints True
# print(s.push(3))#prints True
# print(s.push(4))#prints True
# print(s.push(5))#prints True
# print(s.push(6))#prints True
# print(s.push(7))#prints True
# print(s.push(8))#prints True
# print(s.push(9))#prints Stack Full!
# print(s.size())#prints 8        
# print(s.pop())#prints 8
# print(s.pop())#prints 7
#directed weighted graph class
class Graph(Edge):
    def __init__(self, numV, adj):
        self.numV = numV
        self.adj[][] = adj

    def getNumV(self):
        return self.numV
    
    def setNumV(self, v):
        self.numV = v
    
    ##function that takes 2 vertices and returns edge connecting or null if not adjacent
    def getEdge(self, v1, v2):
        pass
    
    def addEdge(self, weight):

       # newEdge = Edge(weight)
        pass

    ##function to return all (outgoing) edges of a vertex
    def incidentEdges(self, v):
        pass 


#######MAIN############
##calculate adjacency list of vertex and edges[]
a = Vertex("A")
b = Vertex("B")
c = Vertex("C")
d = Vertex("D")
adjList = LinkedList()
