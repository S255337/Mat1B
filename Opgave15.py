from Opgave5 import make_web


def rank_update(web, ranks, page, d):
    n = len(web)
    
    new_rank = (1 - d) / n

    for other, links in web.items():
        if not links:
            # dangling page
            new_rank += d * (ranks[other] / n)
        elif page in links:
            new_rank += d * (ranks[other] / len(links))

    change = abs(new_rank - ranks[page])
    ranks[page] = new_rank

    return change


def recursive_pagerank(web, tol=1e-4, max_iter=200, d=0.85):
    n = len(web)

    # Starter med lige fordeling
    ranks = {page: 1 / n for page in web}

    for i in range(max_iter):
        max_change = 0

        for page in web:
            change = rank_update(web, ranks, page, d)
            max_change = max(max_change, change)

        if max_change < tol:
            return ranks, i + 1

    return ranks, max_iter


# Test
W1 = {0: {2, 4}, 1: {3, 4}, 2: {0}, 3: {0, 1, 4}, 4: set()}
W2 = {0: {1}, 1: {2}, 2: {0}, 3: {4}, 4: {5}, 5: {3}}

print("W1:")
r1, it1 = recursive_pagerank(W1)
print("Result:", r1, "iterationer:", it1)

print("\nW2:")
r2, it2 = recursive_pagerank(W2)
print("Result:", r2, "iterationer:", it2)