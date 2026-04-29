import numpy as np
from Opgave17 import modified_link_matrix

def eigenvector_PageRank(web, d=0.85):
    
    ranking = dict()
    
    pagelist = list(web.keys())
    
    # Vi laver den modificerede link matrix (M)
    M = modified_link_matrix(web, pagelist, d)
    
    # Så finder vi egenværdier og egenvektorer
    eigvals, eigvecs = np.linalg.eig(M)
    
    # Finder egenværdi tættest på 1
    index = np.argmin(np.abs(eigvals - 1))
    
    # Vi tager den tilsvarende egenvektor
    v = eigvecs[:, index]
    
    # Tager kun den reelle del
    v = np.real(v)
    
    # Sørg for at alle værdier er positive, da PageRank skal være positiv
    if np.sum(v) < 0:
        v = -v
    
    # Normaliser så summen bliver 1
    v = v / np.sum(v)
    
    # Så laver vi et dictionary for at matche hver side med dens PageRank værdi
    for i in range(len(pagelist)):
        ranking[pagelist[i]] = v[i]
    
    return ranking

web = {0: {2, 4}, 1: {3, 4}, 2: {0}, 3: {0, 1, 4}, 4: set()} 

ranking = eigenvector_PageRank(web)

# Printer PageRank værdierne for hver side
for page, value in ranking.items():
    print(f"{page}: {value:.4f}")

