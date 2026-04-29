import numpy as np

def surf_step(web, page):

    distribution = dict()
    pages = list(web.keys())
    n = len(pages)
    
    # Her laver vi et array til at holde sandsynlighederne for at lande på hver side
    probability = np.zeros(n)
    links = web.get(page, [])
    
    if len(links) == 0:
        # Hvis der ingen links er, så er sandsynligheden ligeligt fordelt
        probability[:] = 1 / n
    else:
        # Vi laver et for loop til at sætte sandsynlighederne for de sider, der er linket til
        for i in range(n):
            if pages[i] in links:
                probability[i] = 1 / len(links)

    # Vi laver et dictionary hvor nøglerne er siderne og værdierne er sandsynlighederne
    for i in range(n):
        distribution[pages[i]] = probability[i]
        
    return distribution

# Eksempel hvor vi tester ovenstående funktion og tjekker sandsynlighederne for at lande på hver side
web = {0: {2, 4}, 1: {3, 4}, 2: {0}, 3: {0, 1, 4}, 4: set()}

result = surf_step(web, 0)

print(result)