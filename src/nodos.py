#!/usr/bin/env python3
#
#
#       Copyright 2026 Alejandro Gomez
#
#       This program is free software: you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation, either version 3 of the License, or
#       (at your option) any later version.
#
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#       You should have received a copy of the GNU General Public License
#       along with this program.  If not, see <http://www.gnu.org/licenses/>.

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
