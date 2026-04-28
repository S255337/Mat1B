import numpy as np

def surf_step(web, page):

    distribution = dict()
    
    pages = list(web.keys())
    n = len(pages)
    
    #Laver et array til sandsynligheder
    probs = np.zeros(n)
    
    links = web.get(page, [])
    
    if len(links) == 0:
        # Hvis der ingen links er, så er sandsynligheden ligeligt fordelt
        probs[:] = 1 / n
    else:
        # Fordeler sandsynligheden ligeligt på alle sider
        for link in links:
            i = pages.index(link)
            probs[i] = 1 / len(links)
    
    # Laver en dictionary med sider og deres sandsynligheder
    for i in range(n):
        distribution[pages[i]] = probs[i]
    
    return distribution