import numpy as np
from Opgave9 import surf_step

def random_surf(web, n):

    ranking = dict()
    
    # Her begynder vi ranking for hver side
    for page in web:
        ranking[page] = 0

    pages = list(web.keys())
    
    # Vi vælger en tilfældig side af starte på
    current_page = np.random.choice(pages)
    
    # Vi laver et loop for at tjekke hvilke side vi lander på efter n antal steps
    for i in range(n):
        
        # Vi opdaterer ranking for den nuværende side
        ranking[current_page] += 1
        
        # Her bruger vi surf_step til at kunne udregne sandsynligheden for at lande på hver side
        distribution = surf_step(web, current_page)
        
        next_pages = list(distribution.keys())
        probability = list(distribution.values())
        
        # Vi vælger den næste side baseret på sandsynlighederne
        current_page = np.random.choice(next_pages, p=probability)
    
    # Her til sidst slutter vi loopet og finder den endelige ranking ved at dividere antallet af gange vi har landet på hver side  med n, hvor n er det antal af step vi har taget
    for page in ranking:
        ranking[page] = ranking[page] / n

    return ranking