import numpy as np
import matplotlib.pyplot as plt

from Opgave10 import random_surf


def plot_ranking(web, ranking, d=0.85):
    pages = list(web)
    n = len(pages)

    pos = {}
    for i, p in enumerate(pages):
        angle = 2 * np.pi * i / n
        pos[p] = (np.cos(angle), np.sin(angle))

    sizes = [3000 * ranking[p] + 100 for p in pages]

    for i, p in enumerate(pages):
        x, y = pos[p]
        plt.scatter(x, y, s=sizes[i])
        plt.text(x, y, str(p))

    for p, links in web.items():
        x0, y0 = pos[p]

        for link in links:
            x1, y1 = pos[link]
            dx, dy = x1 - x0, y1 - y0

            plt.arrow(x0, y0, dx * 0.8, dy * 0.8, head_width=0.05)

    plt.title("PageRank graf")
    plt.axis("off")
    plt.show()


# test
web = {0: {2, 4}, 1: {3, 4}, 2: {0}, 3: {0, 1, 4}, 4: set()}

ranking = random_surf(web, 10000)

plot_ranking(web, ranking)