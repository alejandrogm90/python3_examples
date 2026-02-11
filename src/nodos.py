import networkx as nx
import matplotlib.pyplot as plt

# Crear un grafo vacío
G = nx.Graph()

# Agregar nodos
G.add_node("A")
G.add_node("B")
G.add_node("C")
G.add_node("D")
G.add_node("E")

# Agregar aristas
G.add_edge("A", "B")
G.add_edge("B", "C")
G.add_edge("C", "A")
G.add_edge("D", "B")
G.add_edge("E", "B")
G.add_edge("E", "C")

# Verificar si existe un nodo
print("¿El grafo contiene el nodo 'A'?", "A" in G)

# Verificar si existe una arista
print("¿El grafo contiene la arista 'A-B'?", G.has_edge("A", "B"))

# Obtener los vecinos de un nodo
print("Vecinos del nodo 'A':", list(G.neighbors("A")))

# Dibujar el grafo
nx.draw(G, with_labels=True)
plt.show()
