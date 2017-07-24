from recommend import *



restaurants1 = [
        make_restaurant('A', [-3, -4], [], 3, [make_review('A', 2)]),
        make_restaurant('B', [1, -1],  [], 1, [make_review('B', 1)]),
        make_restaurant('C', [2, -4],  [], 1, [make_review('C', 5)])
    ]

print(find_centroid(restaurants1))
