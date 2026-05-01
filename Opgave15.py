from Opgave5 import make_web


def rank_update(web, PageRanks, page, d):

    number_of_pages = len(web)
    new_rank = (1 - d) / number_of_pages

    for other_page in web:
        outgoing_links = web[other_page]
        if len(outgoing_links) == 0:
            contribution = PageRanks[other_page] / number_of_pages
            new_rank += d * contribution

        elif page in outgoing_links:
            contribution = PageRanks[other_page] / len(outgoing_links)
            new_rank += d * contribution
    increment = abs(new_rank - PageRanks[page])

    print("Increment for page", page, ":", increment)

    PageRanks[page] = new_rank

    return increment


def recursive_PageRank(web, stopvalue=0.0001, max_iterations=200, d=0.85):
    number_of_pages = len(web)

    PageRanks = dict()

    for page in web:
        PageRanks[page] = 1 / number_of_pages

    iteration = 0

    while iteration < max_iterations:
        largest_change = 0 

        for page in web:
            change = rank_update(web, PageRanks, page, d)
            if change > largest_change:
                largest_change = change

        iteration += 1

        if largest_change < stopvalue:
            break

    return PageRanks, iteration

W1 = {0: {2, 4}, 1: {3, 4}, 2: {0}, 3: {0, 1, 4}, 4: set()}
W2 = {0: {1}, 1: {2}, 2: {0}, 3: {4}, 4: {5}, 5: {3}}

print("W1:")
ranks1, it1 = recursive_PageRank(W1)
print("Result:", ranks1, "iterationer:", it1)

print("\nW2:")
ranks2, it2 = recursive_PageRank(W2)
print("Result:", ranks2, "iterationer:", it2)