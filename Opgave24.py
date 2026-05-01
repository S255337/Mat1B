import numpy as np
from Opgave17 import modified_link_matrix


def eigenvector_PageRank(web, d=0.85):
    ranking = dict()

    pages = list(web)
    
    M = modified_link_matrix(web, pages, d)

    eigvals, eigvecs = np.linalg.eig(M)

    # Finder egenværdi tættest på 1
    idx = np.argmin(np.abs(eigvals - 1))
    v = eigvecs[:, idx]

    v = np.real(v)

    if sum(v) < 0:
        v = -v

    v = v / sum(v)

    for i, page in enumerate(pages):
        ranking[page] = v[i]

    return ranking