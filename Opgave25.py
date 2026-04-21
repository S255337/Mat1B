import numpy as np
import time

from Opgave5 import make_web
from Opgave17 import modified_link_matrix

def pagerank_numpy(web, d=0.85, tolerance=1e-8, max_iter=100):
    pagelist = list(web.keys())
    n = len(pagelist)
    
    # Laver link-matricen
    M = modified_link_matrix(web, pagelist, d)
    
    # Initialiserer PageRank vektoren til at være ens for alle sider
    v = np.ones(n) / n
    
    for i in range(max_iter):
        v_new = M @ v
        
        # Stopper hvis ændringen i vektoren er mindre end tolerance, da det betyder at vi er tæt på konvergens og dermed har fundet en stabil PageRank
        if np.linalg.norm(v_new - v, 1) < tolerance:
            break
        
        v = v_new
    
    # Normaliserer vektoren, så den summerer til 1.
    v = v / np.sum(v)
    
    ranking = {}
    for i in range(n):
        ranking[pagelist[i]] = v[i]
    
    return ranking


# Test af hastighed
start = time.time()
web = make_web(5000, 10, 0)
ranking = pagerank_numpy(web)
end = time.time()

print("Tid til at lave web:", end - start, "sek")

start = time.time()
ranking = pagerank_numpy(web)
end = time.time()

print("Tid til at beregne PageRank:", end - start, "sek")