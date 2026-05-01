import numpy as np

from Opgave5 import make_web
from Opgave17 import modified_link_matrix


def matrix_PageRank(web, power, d=0.85):
    ranking = dict()

    pages = list(web)
    n = len(pages)

    M = modified_link_matrix(web, pages, d)

    M_power = np.linalg.matrix_power(M, power)

    # start med lige fordeling
    v = np.ones(n) / n

    v = M_power @ v

    v = v / v.sum()

    for i, page in enumerate(pages):
        ranking[page] = v[i]

    return ranking


# test
web = {0: {2, 4}, 1: {3, 4}, 2: {0}, 3: {0, 1, 4}, 4: set()}

ranking = matrix_PageRank(web, power=10)
print(ranking)