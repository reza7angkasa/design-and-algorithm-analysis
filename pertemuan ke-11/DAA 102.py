class graph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict=[]
        self.gdict=gdict
    def getVertices(self):
        return list(self.gdict.keys())
    def addVertex(self, vrtx):
       if vrtx not in self.gdict:
            self.gdict[vrtx]=[]

graph_elements={"R":["O","L"],
       "O":["R","M",'P'],
       "M":["O","N"],
       "N":["M","P"],
       "P":["N",'O','L'],
       "L":["R",'P']
               }
g=graph(graph_elements)
g.addVertex('Q')
print(g.getVertices())

