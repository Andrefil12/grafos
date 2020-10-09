import networkx as nx
import matplotlib.pyplot as plt
import numpy as np 

# Exemplo 1

# Gráfico dos nós A,B,C,D sem ligação
DG = nx.DiGraph()
DG.add_nodes_from("ABCD")
nx.draw(DG,with_labels=True)
plt.show()

''' 
Print para demonstrar que sem ligações 
não havendo liagações entre os nós 
todos são igualmente importantes.
'''
pr = nx.pagerank(DG, alpha=0.85)
print(pr)

# Grafico do nós A,B,C,D com ligação
DG.add_weighted_edges_from([("A","B",1), ("B","C",1), ("C","D",1), ("D","A",1)])
nx.draw(DG,with_labels=True)
plt.show()

# Matriz dos links 
A = np.matrix([(0,0,0,1), (1,0,0,0), (0,1,0,0), (0,0,1,0)])
print(A)

# Exemplo 2
#Gráficos com os nós 1,2,3,4
DG_test = nx.DiGraph()
DG_test.add_nodes_from([1,2,3,4])
DG_test.add_weighted_edges_from([(1,3,1), (1,4, 1),(1,2,1),(2,3,1),(2,4,1),(3,1,1),(4,1,1),(4,3,1)])
nx.draw(DG_test, with_labels=True)
plt.show()

# Matriz dos links do exemplo 2
B=np.matrix([(0,0,1,0.5),(1/3,0,0,0),(1/3,0.5,0,0.5),(1/3,0.5,0,0)])
print(B)

# Print com valor alpha=1 
pr=nx.pagerank(DG_test,alpha=1)
print(pr)

# Interação k=1000
np.array((B**1000)*A.T)

# Gráfico de uma rede com 10 nós 

G=nx.fast_gnp_random_graph(10,0.5,directed=True)
nx.draw(G,with_labels=True)
plt.show()

pr=nx.pagerank(G,alpha=0.85)
rank_vector=np.array([[*pr.values()]])
best_node=np.argmax(rank_vector)
print("The most popular website is {}".format(best_node))
