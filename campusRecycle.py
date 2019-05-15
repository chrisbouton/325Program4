#Christopher Bouton and A.....
#Dr. Lori
#Advanced Data Structures 325
#Program 4: Campus Recycling

import csv

#data = vertex
class Vertex():
    def __init__(self, data, index):
        self.data = data
        self.edges = LinkedList()
        self.found = False
        self.index = index
        
    def getData(self):
        return self.data

    def setData(self, data):
        self.data = data
    

class Edge:
    def __init__(self, weight, origin=None, dest=None):
        self.origin = origin
        self.dest = dest
        self.weight = weight
       # self.node = Node()
    
    def getWeight(self):
        return self.weight
    
    def setWeight(self, w):
        self.weight = w
    
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

    # def iterate(self):
    #     self.curr = self.head
    #     i = 0
    #     while(i < self.numItems):


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
class Graph:
    
    def __init__(self, numv, adj, buildings):
        self.Vertices = []
        self.numV = numv
        self.buildings = buildings
        self.adj = adj
        #iterating through matrix and creating vertex and edge objects
        i = 0
        j = 0
        while(i < numv):
            self.Vertices.append(Vertex(buildings[i], i))
            
            while(j < numv):
                if(adj[i][j] != 1000 or adj[i][j] != 0):
                    z = Edge(adj[i][j], i, j)
                    self.Vertices[i].edges.push(z)

                j = j + 1
            i = i + 1

       

    def getNumV(self):
        return self.numV
    
    def setNumV(self, v):
        self.numV = v
    
    ##function that takes 2 vertices and returns edge connecting or null if not adjacent
    #returns edge that is going out of v1 to v2
    def getEdge(self, v1, v2):
        j = 0
        while(v1.edges.goTo(j).dest != None):
            if(v1.edges.goTo(j).dest == v2.index):
                return v1.edges.goTo(j)
            j = j+1
            
        return None

    #returns vertex based on index provided
    def getVertex(self, index):
        for vertex in self.Vertices:
            if (vertex.index == index):
                return vertex
        return None
    
    def addEdge(self, weight):

       # happens in constructor
        pass

    ##function to return all (outgoing) edges of a vertex in a list of the edge objects
    def incidentEdges(self, v):
        incidentEdgeList = []
        j = 0
        while(v.edges.goTo(j) != None):
            incidentEdgeList.append(v.edges.goTo(j))
        return incidentEdgeList

    #depth first search function 
    def DFS(self, startV, numV):
        stack = Stack(numV)

        ##bool array to keep track of visted vertices
        seen = [False] * numV
        seen[startV.index] = True
        stack.push(startV)
        while (stack.size() != 0):
            # Pop new node from stack
            curV = stack.pop()
            # Visit new node
            # ??? 
            # Get neighbors
            edges = curV.edges
            i = 0
            while (i < edges.numItems):
                # Get index of destination at edge with index i
                # then returns vertex object corresponding to that index, outgoing edges btw
                neighbor = self.getVertex(edges.goTo(i).data.getDest())
                if (seen[neighbor.index] == False):
                    seen[neighbor.index] = True
                    stack.push(neighbor)
                i += 1
        print(seen)
        return ()

    def BFS(self, startV, numV):
        queue = Queue()
        seen = [False] * numV
        seen[startV.index] = True
        queue.enqueue(startV)
        while (queue.length != 0):
            curV = queue.dequeue()
            # Visit new node
            # ???
            # Get neighbor's Linked List
            edges = curV.edges
            i = 0 
            while (i < edges.numItems):
                # Get index of destination at edge with index i
                # then returns vertex object corresponding to that index
                neighbor = self.getVertex(edges.goTo(i).data.getDest())
                if (seen[neighbor.index] == False):
                    seen[neighbor.index] = True
                    queue.enqueue(neighbor)
                i += 1
        print(seen)
        return ()

    def Dijkstra(self, source, prevCost, currPath):
        for index, in enumerate(self.Vertices):
            if ((self.adj[source][index] + prevCost < 1000) and (self.adj[source][index] + prevCost) < cost[index]):
                cost[index] = self.adj[source][index] + prevCost
                sinktree[index] = currPath + "," + buildings[index]

                #For each of the primary neighbors, run the Dijkstra algorithm again to 
                #check for additional paths
                self.Dijkstra(index, cost[index], sinktree[index])

            #basically BFS
            #check neighbors of neighbors
            index = 0
            curEdges = self.Vertices[source].edges
            while (index < curEdges.numItems):
                curEdge = curEdges.goTo(index).data
                neighborIndex = curEdge.dest
                #neighbor = self.getVertex(neighborIndex)
                #If the node is a neighbor of a neighbor and the overall cost is less than the 
                #current cost, then it is a shorter path:
                if ((cost[index] + curEdge.weight + prevCost) < 1000) and ((cost[index] + curEdge.weight + prevCost) < cost[neighborIndex]):
                    cost[neighborIndex] = cost[index] + curEdge.weight + prevCost	
                    sinktree[neighborIndex] = sinktree[index] + buildings[neighborIndex]

                    #For each of the neighbor's neighbors, run the Dijkstra function again
                    #to check for additional paths
                    self.Dijkstra(neighborIndex, cost[neighborIndex], sinktree[neighborIndex])
                index += 1
        return sinktree





        # #set all costs to "inf"
        # cost = [1000]* (self.numV)
        # #Set all paths to blank:
        # sinktree = [-1]*(self.numV)
        # #array to keep track of visited vertices
        # #known = [False] * (self.numV)

        # cost[source] = 0
        # sinktree[source] = self.buildings[source]

        # # Get source Vertex:
        # sourceV = self.getVertex(source)
        # #Check for primary neighbors:
		# #If there is a direct cost to source, then it is a primary neighbor and
		# #if the direct cost is less than the current, the path is shorter:
        # #VISIT each node
       
        # queue = Queue()
        # seen = [False] * numV
        # seen[source] = True
        # queue.enqueue(self.Vertices[source])
        # while (queue.length != 0):
        #     curV = queue.dequeue()
        #     # Visit new node
        #     if(((self.getEdge(sourceV, curV).weight + prevCost) < 1000) and (self.getEdge(sourceV, curV).weight + prevCost) < cost[curV.index]):
        #         cost[curV.index] = self.getEdge(sourceV, curV).weight + prevCost
        #         sinktree[index] = currPath + str(curV.index)
        #     # Get neighbor's Linked List
        #     edges = curV.edges
        #     i = 0 
        #     while (i < edges.numItems):
        #         # Get index of destination at edge with index i
        #         # then returns vertex object corresponding to that index
        #         neighbor = self.getVertex(edges.goTo(i).data.getDest())
        #         if (seen[neighbor.index] == False):
        #             seen[neighbor.index] = True
        #             queue.enqueue(neighbor)
        #         i += 1

        
#######MAIN############
##open csv files with vertices and edges of La tech main campus academic buildings
##make adjacency list with indexes corresponding to vertices
numV = 18
adjMatrix = []
buildings = []
with open('AdjMatrix.csv', "r") as adjmat:
    reader = csv.reader(adjmat, delimiter=',')

    next(reader, None) #skip first row

    #remove letters from array rows and store in vertices
    for row in reader:
        buildings.append(row[0])
        adjMatrix.append(row[1:19])

    #skips the first row

#convert to int
adjMatrix = [[int(j) for j in i] for i in adjMatrix]

# print (buildings)
# print (adjMatrix)
##command to intiate static graph of buildings in the constructor of Graph
gang = Graph(numV, adjMatrix, buildings)
gang.BFS(gang.Vertices[0], numV)
gang.DFS(gang.Vertices[0], numV)
#print (gang.DFS(gang.Vertices[0], numV))

##dijkstras 
k = 0
for build in buildings:
    print ("{}={}".format(build, k))
    k +=1
#set all costs to "inf"
cost = [1000]* (gang.numV)
#Set all paths to blank:
sinktree = [-1]*(gang.numV)
print("################")
dij = input("Enter start building's index for Dijkstras algorithim\n")
dij = int(dij)
cost[dij] = 0
sinktree[dij] = gang.buildings[dij]
x = gang.Dijkstra(dij, 0, buildings[dij])
i = 0
for item in x:
    print("Path: {}".format(item))
    print("{} 10ths of a mile".format(cost[i]))
    i += 1





