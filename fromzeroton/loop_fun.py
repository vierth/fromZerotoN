# Loops allow us to execute code again and again

# While loop. execute as long as some statement is true.
i = 0 # this followed often by j, k
while i < 10:
    print(f"{i} is less than 10")
    #print(i, "is less than 10")
    #print(str(i) + " is less than 10")
    # i = i + 1
    i += 1

# for loop iterates through an iterable
int_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in int_list:
    print(f"{i} is in int_list (for loop)")

# range() function
for i in range(10):
    print(f"{i} with range function")

# range() function
for i in range(3,12):
    print(f"{i} with range function 3 to 11")

# range() function
for i in range(4,20,2):
    print(f"{i} with range function 4 to 20 by 2")

# range() function
for i in range(10,0,-1):
    i += 20
    print(f"{i} with range function")

letter_list = ["a", "b", 15,"d","e"]
for letter in letter_list:
    print(letter)

my_string = "chugalug"
for airplane in my_string:
    print(airplane)

for letter in letter_list:
    print(letter)
    if letter == "d":
        print("found d!")

for i,letter in enumerate(my_string):
    print(i, letter)

total_loops = 0
for i in range(10):
    for j in range(10):
        for k in range(11):
            print(i, j)
            total_loops +=1

print(total_loops, "total loop")