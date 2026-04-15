import numpy as np

def rank_update(web, PageRanks, old_ranks, page, d):

    N = len(web)
    new_rank = (1 - d) / N

    for q in web:

        # link contribution
        if page in web[q] and len(web[q]) > 0:
            new_rank += d * old_ranks[q] / len(web[q])

        # sink nodes (no outgoing links)
        if len(web[q]) == 0:
            new_rank += d * old_ranks[q] / N

    increment = abs(PageRanks[page] - new_rank)
    PageRanks[page] = new_rank

    return increment


def recursive_PageRank(web, stopvalue=0.0001, max_iterations=200, d=0.85):

    N = len(web)

    PageRanks = {page: 1 / N for page in web}

    iteration = 0

    for _ in range(max_iterations):

        old_ranks = PageRanks.copy()
        max_change = 0

        for page in web:
            inc = rank_update(web, PageRanks, old_ranks, page, d)
            max_change = max(max_change, inc)

        iteration += 1

        if max_change < stopvalue:
            break

    return PageRanks, iteration
web = {
    0: {1, 2},
    1: {2},
    2: {0},
    3: set()
}

ranks, iters = recursive_PageRank(web)

print("PageRanks:", ranks)
print("Iterations:", iters)