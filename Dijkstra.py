#Dijkstra's Algorithm Program
#By Dakota Digilormo

#Import libraries:
import csv 
from enum import IntEnum

#Declare variables:
nodemain = ''
nodeinfo = []
cost = []
sinktree = []

class Nodes(IntEnum):
	A = 0
	B = 1
	C = 2
	D = 3
	E = 4
	F = 5
	G = 6
	H = 7
	I = 8
	J = 9

	
#Dijkstra Algorithm function:
def Dijkstra (source, prevcost, currentpath):

	#Visit each node:
	for index, node in enumerate(nodeinfo):
		#Check for primary neighbors:
		#If there is a direct cost to source, then it is a primary neighbor and
		#if the direct cost is less than the current, the path is shorter:
		if ((nodeinfo[source][index] + prevcost) < 1000) and ((nodeinfo[source][index] + prevcost) < cost[index]):
			cost[index] = nodeinfo[source][index] + prevcost
			sinktree[index] = currentpath + Nodes(index).name
			
			#For each of the primary neighbors, run the Dijkstra algorithm again to 
			#check for additional paths
			Dijkstra(index, cost[index], sinktree[index])
				
		#Check neighbors of neighbors:
		for neighborindex, neighbor in enumerate(node):
			#If the node is a neighbor of a neighbor and the overall cost is less than the 
			#current cost, then it is a shorter path:
			if ((cost[index] + neighbor + prevcost) < 1000) and ((cost[index] + neighbor + prevcost) < cost[neighborindex]):
				cost[neighborindex] = cost[index] + neighbor + prevcost	
				sinktree[neighborindex] = sinktree[index] + Nodes(neighborindex).name
				
				#For each of the neighbor's neighbors, run the Dijkstra function again
				#to check for additional paths
				Dijkstra(neighborindex, cost[neighborindex], sinktree[neighborindex])
	
	return
	

#Open the LinkStates file and store the information:
with open('LinkStates.csv', newline='') as linkstate:
	linkinfo = csv.reader(linkstate)

	next(linkinfo, None) #Skips the first row	
	
	#Remove letters from array rows and store in nodeinfo:
	for row in linkinfo:
		nodeinfo.append(row[1:11])

#Convert data from string to int: 
nodeinfo = [[int(j) for j in i] for i in nodeinfo]

#Prompt the user for node input:
nodemain = input("Please type the node name and click Enter: \r\n")
currentpath = nodemain

#Dijkstra's Algorithm:

#First run: (No Nodes Visited)
#Set all cost values to infinity (1000):
cost = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]
#Set all paths to blank:
sinktree = ['', '', '', '', '', '', '', '', '', '']

#Source Run:
#Set source node cost to 0:
cost[Nodes[nodemain].value] = 0
#Set source node path to given node:
sinktree[Nodes[nodemain].value] = nodemain

#Algorithm Logic:
#Iterate through remaining nodes:
Dijkstra(Nodes[nodemain].value, 0, nodemain)

#End Dijkstra's Algorithm

#Remove partial sinktree paths:
#Removes an element if it is a substring of another element
sinktree = set(i for i in sinktree if not any(i in j for j in sinktree if i != j))

#Display the source tree:
print("\r\nSource tree for node ", nodemain, ": \r\n")
print(', '.join(sinktree))
print("\r\n")

#Display node cost:
print("Cost for node ", nodemain, ": \r\n")
print("A:", cost[0], ", B:", cost[1], ", C:", cost[2], ", D:", cost[3], ", E:", cost[4],
	", F:", cost[5], ", G:", cost[6], ", H:", cost[7], ", I:", cost[8], ", J:", cost[9], "\r\n")