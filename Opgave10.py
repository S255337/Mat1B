import random

from Opgave9 import surf_step

def random_surf(web, n):
    ranking = dict()
    
    for page in web:
        ranking[page] = 0

    current_page = random.choice(list(web.keys()))

    for _ in range(n):
        ranking[current_page] += 1
        
        distribution = surf_step(web, current_page)
        
        pages = list(distribution.keys())
        probs = list(distribution.values())
        
        current_page = random.choices(pages, probs)[0]

    for page in ranking:
        ranking[page] /= n

    return ranking

#"Hastagsene" er for at køre den ovenstående kode, da det er en del af opgaven at teste den. Du kan ændre "LinkA", "LinkB" og "LinkC" til andre sider for at teste forskellige websider og se, hvordan chancen for at lande på hver side ændrer sig.

    #web = {
    #"LinkA": ["LinkB", "LinkC"], 
    #"LinkB": ["LinkC"],
    #"LinkC": []
#}

#random_surf(web, 10000)