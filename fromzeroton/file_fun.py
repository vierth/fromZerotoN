# reading and writing files is important in Python
# it will help us save the results of our scripts (serialization?)

# Write to file
# BE VERY CARFUL
# This will overwrite a file if it already exists
writefile = open("new_file.txt", "w", encoding="utf8")
writefile.write("This is really cool!")
writefile.close()

# Context manager will close the file when we are done with it
# this is considered the "Pythonic" way of doing this
with open('new_file.txt', 'w', encoding='utf8') as wf:
    wf.write("Hello, writing to file!")
    wf.write("This is more info")

# often we want to read from a file
with open('new_file.txt', 'r', encoding='utf8') as rf:
    text = rf.read()

print(text)

with open('new_file.txt', 'a', encoding='utf8') as af:
    af.write("\n")
    af.write("adding more information")