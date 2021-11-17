import networkx as nx
import matplotlib.pyplot as plt
vertices=range(1,15)
edges=[(4,1),(10,1),(1,2),(12,2),(2,11),(2,15),(2,3),(3,13),(3,5),(2,6),(6,8),(6,14),(6,7),(6,9)]
G= nx.Graph()
G.add_nodes_from(vertices)
G.add_edges_from(edges)
nx.draw(G, with_labels=True, node_color='orange', node_size=800)
print (nx.degree_centrality(G))
print (nx.betweenness_centrality(G))
print (nx.closeness_centrality(G))
centrality=nx.eigenvector_centrality(G)
print (sorted((v, '{:0.2f}' .format(c)) for v, c in centrality.items()))
plt.show()