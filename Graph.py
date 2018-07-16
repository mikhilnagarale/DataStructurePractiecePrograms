#!/usr/bin/python
#Ref : http://interactivepython.org/courselib/static/pythonds/Graphs/Objectives.html
#IMP Topics to cover-
#Vertex/Node
#Edge/Arc
#Directed Graph
#Weight of Edge
#Path
#Cycle
#Acyclic Graph
#DAG - Directed Acyclic Graph
#Graph Implementation - 
# 1) Adjancency Metrix (+ Sparx Matrix Issue due to absence edges) 
# 2)Adjancency List (Implementation using Dictionary)

class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}
        
    #def __str__(self):
        #return str(self.id)+' '+'connected to '+str([x.id for x in self.connectedTo])
    
    def __repr__(self):
        return str(self.id)
        #return str(self.id)+' '+'connected to '+str([x for x in self.connectedTo])
   
    #A Vertex should not be iterate logically. Hense Commenting this method.
    #def __iter__(self):
        #return iter(self.connectedTo.key())

    def addNeighbour(self,nbrVertex,weight=0):
        #if nbrVertex not in self.connectedTo.keys():
        #print ('inside addNeighbour')
        self.connectedTo[nbrVertex] = weight
        
    def getConnections(self):
        return self.connectedTo.keys()
    
    def getWeight(self,nbrVertex):
        if nbrVertex in self.connectedTo.keys():
            return self.connectedTo[nbrVertex]
        else:
            return 0
   
    def getId(self):
        return self.id
    
class Graph:
    def __init__(self):
        self.vertexList = {}
        self.vertexCount = 0
        
    def __repr__(self):
        return str(self.vertexList.values())
        
    def __contains__(self,vertex):
        return vertex in self.vertexList
    
    def addVertex(self,vertex):
        if vertex not in self.vertexList.keys():
            self.vertexCount = self.vertexCount + 1
            V = Vertex(vertex)
            self.vertexList[vertex] = V
            return V

    def getVertex(self,vertex):
        if vertex in self:
            return self.vertexList[vertex]
        else:
            return None
        
    def addEdge(self,vertexFrom,vertexTo,weight=0):
        if vertexFrom not in self:
            self.addVertex(vertexFrom)
        if vertexTo not in self:
            self.addVertex(vertexTo)
        vertexFrom = self.getVertex(vertexFrom)    
        vertexFrom.addNeighbour(vertexTo,weight)
        
    
    def getVertices(self):
        return self.vertexList.keys()
    
    #We're using this method since it helps iterate complex objects
    #A graph is an complex object contains vertexList and vertex count
    #If we want to iterate throug graph means we want to iterate through it's vertex
    #Hense we're defining __iter__ method
    #Use-  Eg- [x for x in graph]
    def __iter__(self):
        print(type(iter(self.vertexList.values())))
        return iter(self.vertexList.values())
    
    def getNextVertex(self):
        for vertex in self.vertexList.values():
            yield vertex
            

if __name__ == "__main__":
    #v = Vertex('A')
    #B = Vertex('B')
    #C = Vertex('C')
    #D = Vertex('D')
    #print(v)
    #v.addNeighbour(B,6)
    #v.addNeighbour(C,8)
    #v.addNeighbour(D,9)
    #print(v)
    #print(v.getWeight(C))
    #print(v.getConnections())
    
    myGraph = Graph()
    A = myGraph.addVertex('A')
    B = myGraph.addVertex('B')
    C = myGraph.addVertex('C')
    D = myGraph.addVertex('D')
    E = myGraph.addVertex('E')

    print(myGraph)
    
    myGraph.addEdge('A','B',9)
    myGraph.addEdge('B','C',10)
    myGraph.addEdge('C','D',11)
    myGraph.addEdge('D','E',12)
    myGraph.addEdge('E','A',13)
    myGraph.addEdge('A','C',20)
    myGraph.addEdge('A','D',21)
    myGraph.addEdge('A','E',22)
    


    print(myGraph)
    print(A)

    
    for v in myGraph:
        #print(v)
        #print(type(v))
        for connVertex in v.getConnections():
            print("%s,%s,%d" % (v.id,connVertex,v.getWeight(connVertex)))
          
        
    myGraph.addEdge('A','C',29)    
    
    for v in myGraph:
        #print(v)
        #print(type(v))
        for connVertex in v.getConnections():
            print("%s,%s,%d" % (v.id,connVertex,v.getWeight(connVertex)))

    print ('Testing generator method getNextVertex() in Graph class. Executing method using next()')
    a = myGraph.getNextVertex()
    print(next(a))
    print(next(a))      
    print ('Testing generator method getNextVertex() in Graph class. Executing method using for loop')
    for vertex in myGraph.getNextVertex():
        print(vertex)
    
