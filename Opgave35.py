import numpy as np

from Opgave5 import make_web
from Opgave17 import modified_link_matrix

def matrix_PageRank(web, power, d=0.85):

    ranking = dict()

    pagelist = list(web.keys())
    N = len(pagelist)

    # Vi laver den modificerede link matrix (M)
    M = modified_link_matrix(web, pagelist, d)

    # Vi beregner M^power, som opgaven vil have os til at gøre
    M_power = np.linalg.matrix_power(M, power)

    # Så starter vi med en startvektor, hvor alle sider har samme PageRank værdi (1/N)
    v = np.ones(N) / N

    # Vi ganger vores M^power med startvektoren for at få vores endelige PageRank værdier
    v = M_power.dot(v)

    # Her normaliserer vi v, så summen af alle PageRank værdier bliver 1
    v = v / sum(v)

    # I for loopet her laver vi et dictionary for at matche hver side med dens PageRank værdi
    for i in range(N):
        ranking[pagelist[i]] = v[i]

    return ranking

web = {0: {2, 4}, 1: {3, 4}, 2: {0}, 3: {0, 1, 4}, 4: set()}


ranking = matrix_PageRank(web, power=10)
print(ranking)