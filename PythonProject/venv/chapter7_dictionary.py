stuff ={"food":15, "energy":100, "calories":10}
print(stuff)

print(stuff.items())
print(stuff.keys())
print(stuff.popitem())
print(stuff)

print(stuff.setdefault("food"))
print(stuff)
print(stuff.setdefault("friends",123))
print(stuff)

new_items={"rocks":3, "arrows":4}
stuff.update(new_items)
print(stuff)

stuff.update(rocks=45,stone=7)
print(stuff)