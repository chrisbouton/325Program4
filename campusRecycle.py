#Christopher Bouton and A.....
#Dr. Lori
#Advanced Data Structures 325
#Program 4: Campus Recycling

class Vertex:
    def __init__(self, data):
        self.data = data
        self.found = False

    def getData(self):
        return self.data

    def setData(self, data):
        self.data = data
    

class Edge:
    def __init__(self, origin, dest, weight):
        self.origin = origin
        self.dest = dest
        self.weight = weight
    
    def getOrigin(self):
        return self.origin

    def setOrigin(self, origin):
        self.origin = origin

    def getDest(self):
        return self.dest
    
    def setDest(self, dest):
        self.dest = dest


