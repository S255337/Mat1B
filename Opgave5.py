import numpy as np

def make_web(n, k, kmin=0):

    assert(k < n), "k skal være mindre end n"
    assert(kmin <= k), "kmin skal være mindre end eller lig med k"
    
    keys = list(range(n))
    web = dict()
    
    for j in keys:
        numlinks = np.random.randint(kmin, k + 1)
        
        # mulige sider (uden j selv)
        possible_links = list(set(keys) - {j})
        
    # vælg numlinks unikke links
        links = set(np.random.choice(possible_links, size=numlinks, replace=False))
        
        web[j] = links
    
    return web