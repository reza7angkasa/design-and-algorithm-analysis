import networkx as nx
G_fb = nx.read_edgelist('/python/facebook_combined.txt', create_using=nx.Graph(),nodetype=int)
print(nx.info(G_fb))