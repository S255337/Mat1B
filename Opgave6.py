import networkx as nx
import matplotlib.pyplot as plt


def visualize_graph(web):
    G = nx.DiGraph()

    for page, links in web.items():
        for link in links:
            G.add_edge(page, link)

    pos = nx.spring_layout(G)

    nx.draw(
        G,
        pos,
        with_labels=True,
        node_size=1800,
        node_color="skyblue"
    )

    plt.show()

# Test
web = {0: {2, 4}, 1: {3, 4}, 2: {0}, 3: {0, 1, 4}, 4: set()}

visualize_graph(web)