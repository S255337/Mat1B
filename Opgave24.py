import numpy as np
from Opgave17 import modified_link_matrix # Henter matrixen fra Opgave17

def eigenvector_PageRank(web, d=0.85):
    # Laver en liste over sider
    pagelist = list(web.keys())
    
    # Laver link matrixen ved at kalde funktionen fra Opgave17
    M = modified_link_matrix(web, pagelist, d)
    
    # Finder egenværdi(er) og egenvektor(er)
    eigvals, eigvecs = np.linalg.eig(M)
    
    # Finder den egenværdi der er tættest på 1
    i = np.argmin(np.abs(eigvals - 1))
    
    # Tager så den fundne egenvektoren
    v = eigvecs[:, i]
    
    # Fjerner evt den imaginære dele, for at få en reel værdi
    v = np.real(v)
    
    # Gør den positiv, da PageRank skal være positiv, da det er en sandsynlighed
    v = np.abs(v)
    
    # Normaliserer vektoren, så den summerer til 1.
    v = v / np.sum(v)
        
    # Laver dictionary med sider og deres PageRank score
    ranking = {}
    for i in range(len(pagelist)):
        ranking[pagelist[i]] = v[i]
    
    return ranking