import numpy as np

def make_web(n, k, kmin=0):

    # Input: n og k er ikke-negative heltal
    # Output: web er en dictionary med n nøgler.
    # Værdien af hver nøgle er en mængde, der er en delmængde af nøglerne.
    
    assert(k < n), "k skal være mindre end n (da man ikke kan linke til sig selv)"
    assert(kmin <= k), "kmin skal være mindre end eller lig med k"
    
    # n nøgler fra 0 til n-1
    keys = list(range(n))
    
    web = dict()
    
    for j in keys:
        # tilfældigt antal links mellem kmin og k (inklusive)
        numlinks = np.random.randint(kmin, k + 1)
        
        # mulige sider at linke til (undgå j selv)
        possible_links = list(set(keys) - {j})
        
        # vælg numlinks unikke links
        links = np.random.choice(possible_links, size=numlinks, replace=False)
        
        web[j] = set(links)
    
    return web