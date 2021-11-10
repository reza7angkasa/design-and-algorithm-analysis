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

graph_elements={"a":["b","c"],
                "b":["a","d"],
                "c":["a","d"],
                "d":["e"],
                "e":["d"]
               }
g=graph(graph_elements)
g.addVertex('f')
print(g.getVertices())
