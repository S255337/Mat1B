def surf_step(web, page):
    distribution = dict()

    links = web.get(page, [])

    if len(links) == 0:
        n = len(web)
        for p in web:
            distribution[p] = 1 / n
    else:
        n = len(links)
        for p in links:
            distribution[p] = 1 / n

    return distribution

#web = {
##    "LinkA": ["LinkB", "LinkC"], 
##    "LinkB": ["LinkC"],
##    "LinkC": []
##}

## surf_step(web, "LinkA") #Ændre "LinkA" til "LinkB" eller "LinkC" for at teste andre sider, og hvad chancen for den næste side er. 