import networkx as nx
import matplotlib.pyplot as plt

edges=[('lisa','allen'),('allen','liz'),('liz','emma'),('emma','mike'),('mike','bob'),('bob','john'),('john','leah'),('leah','shane'),('shane','liz'),('shane','emma'),('jill','shane'),('jill','emma'),('jill','bob'),('jill','john'),('jill','leah'),('jill','mike'),('bob','emma'),('john','shane')]
G= nx.Graph()

G.add_edges_from(edges)
nx.draw(G, with_labels=True, node_size=800)
print (nx.degree_centrality(G))
print (nx.betweenness_centrality(G))
print (nx.closeness_centrality(G))
centrality=nx.eigenvector_centrality(G)
print (sorted((v, '{:0.2f}' .format(c)) for v, c in centrality.items()))
plt.show()