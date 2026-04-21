import numpy as np
from Opgave17 import modified_link_matrix

def matrix_PageRank(web, power, d=0.85):

    ranking = dict() 

    pages = list(web.keys())
    N = len(pages)

    M = modified_link_matrix(web, pages, d)
    M = np.linalg.matrix_power(M, power)

    v = np.ones(N) / N
    v = np.dot(M, v)

    for i in range(N):
        ranking[pages[i]] = v[i]

    return ranking

# Test af hastighed
w1 = {
    "A": ["B"],
    "B": ["C"],
    "C": ["A"]
}

w2 = {
    "A": ["B", "C"],
    "B": ["C"],
    "C": []
}

print(matrix_PageRank(w1, 10))
print(matrix_PageRank(w2, 10))