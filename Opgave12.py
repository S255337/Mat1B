import numpy as np

def surf_step_damp(web, page, d):
    
    distribution = dict()
    
    pages = list(web.keys())
    N = len(pages)
    
    probs = np.zeros(N)
    
    links = web.get(page, [])
    
    if len(links) == 0:
        # Hvis der ingen links er, så er sandsynligheden ligeligt fordelt
        probs[:] = 1 / N
    else:
        # Start med at fordele (1-d) ligeligt på alle sider
        probs[:] = (1 - d) / N
        
        # Fordel d på de sider der linkes til
        for link in links:
            i = pages.index(link)
            probs[i] += d / len(links)
    
    # Her laver vi en dictionary med sider og deres sandsynligheder
    for i in range(N):
        distribution[pages[i]] = probs[i]
    
    return distribution

def random_surf_damp(web, n, d):
    
    ranking = dict()
    
    for p in web:
        ranking[p] = 0

    pages = list(web.keys())
    
    # Start med at vælge en tilfældig startside
    current_page = np.random.choice(pages)
    
    for i in range(n):
        
        ranking[current_page] += 1
        
        distribution = surf_step_damp(web, current_page, d)
        
        next_pages = list(distribution.keys())
        probs = list(distribution.values())
        
        current_page = np.random.choice(next_pages, p=probs)
    
    # Gør det til sandsynligheder (PageRank)
    for p in ranking:
        ranking[p] = ranking[p] / n
    
    return ranking