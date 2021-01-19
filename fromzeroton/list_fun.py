# lists!
# an ordered container for information/python objects

# create a list with square brackets and each item is seperated
# with a comma
name_list = ["Juan", "Rogier", "Ying", "Cindy"]

# a list can be empty
empty_list = []

# can contain basic data types
int_list = [1, 2, 3, 4, 5, 6, 7]
float_list = [1.0, 3.4, -.5]

# you can mix datatypes
mixed_list = [1, "hello", 4.4]

# you can have lists of lists
list_list = [[1,3], [2,4,6], ["tree", "rock", "boat", "gorge"]]

# lists always keep the same order
int_list = [4, 12, -1, 2, 5]

#print first item
print(int_list[0])
# print last item
print(int_list[-1])
# get a slice from a list
print(int_list[2:4])
# get index of -1
print(int_list.index(-1))
# change value in list
int_list[2] = 10
print(int_list)

# add an item to a list
int_list.append(6)
print(int_list)

# remove item from list
removed_value = int_list.pop(1)
print(int_list)
print(removed_value)

# add value at index
int_list.insert(1,42)
print(int_list)

# we can turn strings into lists
greeting = "Hello, my name is Paul"

# Turn into a list
greeting_list = list(greeting)
print(greeting_list)

# more turn into list
greeting_words = greeting.split(" ")
print(greeting_words)

# turn back into list
new_greeting = " ".join(greeting_words)
print(new_greeting)

# get the lenght of a list
len(int_list)
min(int_list)
max(int_list)
int_list.reverse()
print(int_list)
int_list.sort(reverse=True)
print(int_list)

name_list.sort()
print(name_list)