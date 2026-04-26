import numpy as np

def make_web(n, k, kmin=0):

    assert(k < n)
    assert(kmin <= k)
    
    keys = list(range(n))
    web = dict()
    
    #Vælger den vigtig side
    important_page = np.random.choice(keys)
    
    for j in keys:
        numlinks = np.random.randint(kmin, k + 1)
        possible_links = list(set(keys) - {j})
        
        #80% chance for at pege på vigtig side
        links = set()
        
        for _ in range(numlinks):
            if np.random.rand() < 0.8:
                links.add(important_page)
            else:
                links.add(np.random.choice(possible_links))
        
        # undgå self-loop
        links.discard(j)
        
        web[j] = links
    
    return web