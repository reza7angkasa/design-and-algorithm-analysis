class graph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict=[]
        self.gdict=gdict
    def getVertices(self):
        return list(self.gdict.keys())
graph_elements={"R":["O","L"],
       "O":["R","M",'P'],
       "M":["O","N"],
       "N":["M","P"],
       "P":["N",'O','L'],
       "L":["R",'P']
               }
g=graph(graph_elements)
print(g.getVertices())



