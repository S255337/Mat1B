import numpy as np

def rank_update(web, PageRanks, page, d):
    
    # Hvor mange sider er der i alt
    number_of_pages = len(web)
    
    # Start med den del hvor man hopper tilfældigt
    new_rank_value = (1 - d) / number_of_pages
    
    # Kig på alle sider i nettet
    for other_page in web:
        
        # Hvis der er et link til den side vi kigger på
        if page in web[other_page] and len(web[other_page]) > 0:
            new_rank_value += d * PageRanks[other_page] / len(web[other_page])
        
        # Hvis siden ikke har nogen links (sink)
        if len(web[other_page]) == 0:
            new_rank_value += d * PageRanks[other_page] / number_of_pages
    
    # Hvor meget har værdien ændret sig
    change_in_rank = abs(PageRanks[page] - new_rank_value)
    
    # Opdater værdien
    PageRanks[page] = new_rank_value
    
    return change_in_rank


def recursive_PageRank(web, stop_value=0.0001, max_iterations=200, d=0.85):
    
    # Antal sider
    number_of_pages = len(web)
    
    # Start med at alle sider har samme værdi
    PageRanks = {}
    for page in web:
        PageRanks[page] = 1 / number_of_pages
    
    iteration = 0
    
    # Kør flere gange indtil vi stopper
    for i in range(max_iterations):
        
        biggest_change = 0
        
        # Opdater hver side én ad gangen
        for page in web:
            change = rank_update(web, PageRanks, page, d)
            
            # Gem den største ændring vi ser
            if change > biggest_change:
                biggest_change = change
        
        iteration += 1
        
        # Stop hvis ændringen er meget lille
        if biggest_change < stop_value:
            break
    
    return PageRanks, iteration