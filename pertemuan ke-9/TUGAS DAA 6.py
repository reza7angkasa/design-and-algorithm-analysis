import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
myWeb=nx.DiGraph()
myPages = range(1,5)
connections=[(1,2),(2,3),(3,4),(4,1),(4,5),(5,1)]
myWeb.add_nodes_from(myPages)
myWeb.add_edges_from(connections)
pos=nx.spectral_layout(myWeb)
nx.draw(myWeb, pos, arrows=True, with_labels=True)
plt.show()