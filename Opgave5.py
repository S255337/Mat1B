import networkx as nx
import matplotlib.pyplot as plt

def visualize_graph(web):
    
    G = nx.DiGraph()

    for node, links in web.items():
        for target in links:
            G.add_edge(node, target)

    pos = nx.spring_layout(G)

    nx.draw(
        G,
        pos,
        with_labels=True,
        node_size=2000,
        node_color="lightblue",
        arrows=True
    )

    plt.show()



web = {
    0: {1, 2},
    1: {2},
    2: {0},
    3: set()
}


visualize_graph(web)
