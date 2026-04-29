import numpy as np

def surf_step_damp(web, page, d):
    
    distribution = dict()
    pages = list(web.keys())
    N = len(pages)
    
    probability = np.zeros(N)
    links = web.get(page, [])
    
    if len(links) == 0:
        probability[:] = 1 / N
    else:
        probability[:] = (1 - d) / N
        for link in links:
            i = pages.index(link)
            probability [i] += d / len(links)
    
    for i in range(N):
        distribution[pages[i]] = probability[i]
    
    return distribution



def random_surf_damp(web, n, d):
    
    ranking = dict()
    
    for p in web:
        ranking[p] = 0

    pages = list(web.keys())
    current_page = np.random.choice(pages)
    
    for i in range(n):
        ranking[current_page] += 1
        distribution = surf_step_damp(web, current_page, d)
        
        next_pages = list(distribution.keys())
        probability = list(distribution.values())
        
        current_page = np.random.choice(next_pages, p=probability)
    
    for p in ranking:
        ranking[p] = ranking[p] / n
    
    return ranking