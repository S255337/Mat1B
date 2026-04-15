import random

def surf_step_damp(web, page, d):
    distribution = dict()
    N = len(web)

    links = web.get(page, [])

    if len(links) == 0:
        for p in web:
            distribution[p] = 1 / N
    else:
        for p in web:
            distribution[p] = (1 - d) / N
        
        for link in links:
            distribution[link] += d / len(links)

    return distribution

def random_surf_damp(web, n, d):
    ranking = dict()

    for p in web:
        ranking[p] = 0

    current_page = random.choice(list(web.keys()))

    for _ in range(n):
        ranking[current_page] += 1

        distribution = surf_step_damp(web, current_page, d)

        pages = list(distribution.keys())
        probs = list(distribution.values())

        current_page = random.choices(pages, probs)[0]

    for p in ranking:
        ranking[p] /= n

    return ranking

dist = surf_step_damp({
    "A": ["B", "C"],
    "B": ["C"],
    "C": []
}, "A", 0.85)

print(sum(dist.values()))