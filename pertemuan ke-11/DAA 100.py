class graph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict={}
        self.gdict=gdict
    def edges(self):
        return self.findedges()
    def findedges(self):
        edgename=[]
        for vrtx in self.gdict:
            for nxtvrtx in self.gdict[vrtx]:
                if {nxtvrtx, vrtx} not in edgename:
                    edgename.append({vrtx, nxtvrtx})
        return edgename
graph_elements = {"T":["W","U"],
       "V":["U","X"],
       'U':['V','T'],
       "W":["T","X",'Z'],
       "X":["W","V",'S'],
       "Z":["W"],
       "S":["X"]
                  }
g=graph(graph_elements)
print(g.edges())

