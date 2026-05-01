import numpy as np

def surf_step(web, page):
    distribution = dict()
    pages = list(web.keys())
    n = len(pages)

    probs = np.zeros(n)
    links = web.get(page, set())

    if not links:
        probs[:] = 1 / n
    else:
        share = 1 / len(links)
        for i, p in enumerate(pages):
            if p in links:
                probs[i] = share

    for i, p in enumerate(pages):
        distribution[p] = probs[i]

    return distribution


# Test
web = {0: {2, 4}, 1: {3, 4}, 2: {0}, 3: {0, 1, 4}, 4: set()}

print(surf_step(web, 0))