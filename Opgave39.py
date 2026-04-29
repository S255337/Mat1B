import numpy as np
import matplotlib.pyplot as plt

from Opgave10 import random_surf

def plot_ranking(web, ranking, d=0.85):
    pages = list(web.keys())
    n = len(pages)

    pos = {}
    for i in range(n):
        angle = 2 * np.pi * i / n
        x = np.cos(angle)
        y = np.sin(angle)
        pos[pages[i]] = (x, y)

    sizes = []
    for p in pages:
        sizes.append(3000 * ranking[p] + 100)

    for i in range(n):
        x, y = pos[pages[i]]
        plt.scatter(x, y, s=sizes[i])
        plt.text(x, y, str(pages[i]))

    for p in pages:
        x0, y0 = pos[p]

        for link in web[p]:
            x1, y1 = pos[link]

            dx = x1 - x0
            dy = y1 - y0

            plt.arrow(x0, y0, dx * 0.8, dy * 0.8,
                      head_width=0.05)

    plt.title("PageRank graf")
    plt.axis("off")
    plt.show()

web = {0: {2, 4}, 1: {3, 4}, 2: {0}, 3: {0, 1, 4}, 4: set()}  


ranking = random_surf(web, 10000)

plot_ranking(web, ranking)