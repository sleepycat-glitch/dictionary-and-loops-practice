# this is what we will use for the video intro to dictionaries

# dictionary = collection of {key:value} pairs ordered and changeable, no duplicates

capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

# print(dir(capitals))
# print(help(capitals))

print(capitals.get("USA")) # Washinton D.C.
print(capitals.get("India")) # New Delhi
if print(capitals.get("Japan")):
    print("That capital exists.")
else: 
    print("That capital doesn't exist.")

capitals.update({"Germany": "Berlin"}) # similar to append for lists 
# could also be used to replace values, ex. cpaitals.update({"USA": "Detroit"})
# .pop() in dict are used to delete entire section of dict, ex. capitals.pop("China")
# .popitem() removes last item in dict, ex. capitals.popitem()
# .clear() deletes entire dict, ex. capitals.clear()
print(capitals)

keys = capitals.keys() #returns all keys within dict
print(keys)

# iterate over every key
for key in capitals.keys():
    print(key)

# iterate over every value
values = capitals.values()
for value in capitals.values():
    print(value)

items = capitals.items()
for key, value in capitals.items():
    print(f"{key}: {value}")
