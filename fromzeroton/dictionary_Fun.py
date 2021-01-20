# Dictionaries let you store information using a key, value pair
# create an empty dictionary
my_dict = {}
my_dict = dict()

# create dictionary to keep track of ages:
# keys must be immutable (they can't change)
ages = {"Paul":37, "Padma": 25, "Gorp": 155}

# keep in mind that order is not perserved in older versions of python
# print(ages)
gorp_age = ages["Gorp"]
print(gorp_age)

# add info to the dictionary
ages["Blbobl"] = 20
print(ages)
ages["Paul"] = 25
print(ages)

#ages["Shannon"] #gives a key error

# iterate through keys
for key in ages.keys():
    print(key)
    print(ages[key])

# iterate through values
for value in ages.values():
    print(value)

# iterate through keys and values:
for key, value in ages.items():
    print(key, value)