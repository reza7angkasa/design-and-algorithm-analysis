class graph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict=[]
        self.gdict=gdict
    def getVertices(self):
        return list(self.gdict.keys())
graph_elements={"T":["W","U"],
       "V":["U","X"],
       'U':['V','T'],
       "W":["T","X",'Z'],
       "X":["W","V",'S'],
       "Z":["W"],
       "S":["X"]
               }
g=graph(graph_elements)
print(g.getVertices())
