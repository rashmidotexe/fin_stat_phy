import networkx as nx
import matplotlib.pyplot as plt

# Assuming a simple correlation-based network
correlation_matrix = order_flow_data.corr()  # Simplified for example
threshold = 0.5  # arbitrary threshold

G = nx.Graph()

for col in correlation_matrix.columns:
    for index in correlation_matrix.index:
        if correlation_matrix.loc[index, col] > threshold:
            G.add_edge(index, col)

nx.draw(G, with_labels=True)
plt.show()
