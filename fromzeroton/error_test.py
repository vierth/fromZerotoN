# there are many kinds of errors that we can run into in python
for i in range(20):
    print(i)

a = "hello!"

# keep writing code
b = "hello times 2"

c = 5

my_list = [1, 2, 3, 4, 5, 6]
#print(my_list[100])

my_dict = {"Paul":10, "Shannon":11}
# print(my_dict["Roger"])
try:
    my_list[100]
    my_dict["Roger"]
except KeyError:
    print("person not in dictionary")

#5/0