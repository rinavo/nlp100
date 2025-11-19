str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics"
words = str.split(" ")

print(list(map(lambda e: len(e), words)))
