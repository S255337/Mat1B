import numpy as np
from Opgave9 import surf_step

def random_surf(web, n):

    ranking = dict()
    
    # Her initialiserer vi ranking for hver side til 0
    for page in web:
        ranking[page] = 0

    pages = list(web.keys())
    
    # Vælger en tilfældig startside
    current_page = np.random.choice(pages)
    
    # Laver et loop der kører n gange
    for i in range(n):
        
        # Vi opdaterer ranking for den nuværende side
        ranking[current_page] += 1
        
        # Her bruger vi surf_step til at få sandsynlighedsfordelingen for næste side
        distribution = surf_step(web, current_page)
        
        next_pages = list(distribution.keys())
        probs = list(distribution.values())
        
        # Vi vælger den næste side baseret på sandsynlighederne
        current_page = np.random.choice(next_pages, p=probs)
    
    # Til sidst normaliserer vi ranking ved at dividere med n, så det bliver en fordeling
    for page in ranking:
        ranking[page] = ranking[page] / n

    return ranking