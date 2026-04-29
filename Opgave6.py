import networkx as nx
import matplotlib.pyplot as plt

def visualize_graph(web):

    graph = nx.DiGraph()

    # Her tilføjer vi alle sider som noder i grafen
    for page in web:
        links = web[page]

        # Tilføjer noder og kanter til vores graf
        for link in links:
            graph.add_edge(page, link)

    # Vi laver et layout for grafen, så det ligner PageRank graf
    pos = nx.spring_layout(graph)

    # Her bruger vi nx.draw til at tegne grafen
    nx.draw(graph, pos,
            with_labels=True,
            node_size=1800,
            node_color="skyblue")
    plt.show()


# Eksempel, så man kan se hvordan det ender med at se ud, rent visuelt.
web = {
    0: {1, 2},
    1: {2},
    2: {0},
    3: set()
}

visualize_graph(web)