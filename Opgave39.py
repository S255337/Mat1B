import numpy as np
import matplotlib.pyplot as plt

from Opgave5 import make_web
from Opgave10 import random_surf


def plot_ranking(web, ranking, d=0.85):

    pages = list(web.keys())
    n = len(pages)
    
    pos = {}
    for i in range(n):
        angle = 2 * np.pi * i / n
        pos[pages[i]] = (np.cos(angle), np.sin(angle))
    
    sizes = []
    for p in pages:
        sizes.append(3000 * ranking[p] + 100)
    
    for i in range(n):
        x, y = pos[pages[i]]
        plt.scatter(x, y, s=sizes[i])
        plt.text(x, y, pages[i], ha='center', va='center')
    
    for p in pages:
        x0, y0 = pos[p]
        
        for link in web[p]:
            x1, y1 = pos[link]
            
            dx = x1 - x0
            dy = y1 - y0
            
            plt.arrow(x0, y0, 0.8*dx, 0.8*dy,
                      head_width=0.05,
                      length_includes_head=True)
    
    plt.title("PageRank graf")
    plt.axis('off')
    plt.show()


# Her er en test for at se hvordan det ser ud visuelt, som opgaven beder om. 

web = make_web(5, 2, 0)
ranking = random_surf(web, 10000)

plot_ranking(web, ranking)