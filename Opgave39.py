import numpy as np
import matplotlib.pyplot as plt

from Opgave5 import make_web
from Opgave10 import random_surf


def plot_ranking(web, ranking, d=0.85):
    
    pages = list(web.keys())
    n = len(pages)
    
    # Laver positioner i en cirkel
    theta = []

    for i in range(n):
        vinkel = 2 * np.pi * i / n
        theta.append(vinkel)
    
    pos = {}
    for i in range(n):
        pos[pages[i]] = (np.cos(theta[i]), np.sin(theta[i]))
    
    # Node størrelser (bare skaleret lidt op), så de er synlige og så større PageRank giver større noder
    sizes = []
    for p in pages:
        sizes.append(3000 * ranking[p] + 100)
    
    # tegn noder
    for i in range(n):
        x, y = pos[pages[i]]
        plt.scatter(x, y, s=sizes[i])
        plt.text(x, y, str(pages[i]), ha='center', va='center')
    
    # tegn pile
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

# Test af hastighed (Har selv valgt talene, kan ændres).
#web1 = make_web(5, 3)
#rank1 = random_surf(web1, 10000)

#plot_ranking(web1, rank1)


#web2 = make_web(7, 3)
#rank2 = random_surf(web2, 10000)

#plot_ranking(web2, rank2)