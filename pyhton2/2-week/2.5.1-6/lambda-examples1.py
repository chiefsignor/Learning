bigrams = {"AB": [10, 11, 12], "BC": [5, -5, 8], "CD": [105, 1, 0],
           "DE": [6, 6], "EF": [15, 20, 15], "FG": [22, 11, 32],
           "GH": [20, 20, 20]}
sorter = sorted(bigrams, key=lambda key: sum(bigrams[key]), reverse=True)

for key in sorter:
    print(key, bigrams[key])