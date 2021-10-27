import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
myWeb=nx.DiGraph()
myPages = range(1,4)
connections=[(1,2),(2,1),(2,3),(3,2),(3,4),(4,3),(4,1)]
myWeb.add_nodes_from(myPages)
myWeb.add_edges_from(connections)
pos=nx.spring_layout(myWeb)
nx.draw(myWeb, pos, arrows=True, with_labels=True)
plt.show()

