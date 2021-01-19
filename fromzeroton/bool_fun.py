# boolean operators
# expressions that evaluate to either True or False

# test if two values are equal to each other
5 == 5 # True
"a" == "a" # True
5 == 6 # False

# test if two values are NOT equal to each other
5 != 5 # False
5 != 6 # True

# check if one number is smaller than another
5 < 6 # True
6 < 5 # False

# larger than
5 > 6 # False
6 > 5 # True

# less than or equal to
6 <= 6 # True
6 <= 7 # True
6 <= 5 # False

# greater than or equal to
6 >= 6 # True
6 >= 7 # False
6 >= 5 # True

a = ["hello"]
b = ["hello"]
# print(a == b)
# print(a is b)
c = b
# print(c is b)

# check if item in list
int_list = [1, 2, 3, 4, 5]
#print(6 in int_list)

if 10 > 20:
    # execute this code IF statement is true
    print("Exactly")
    print("hello")

print("Kept going after code block")

if 30 < 20:
    print("hey, isn't it weird that 30 is smaller than 20")
else:
    print('of course, 30 is not smaller than 20')

if 10 > 10:
    a = "10 is larger than 10"
elif 10 == 10:
    a = "10 is 10"
elif 10 < 10:
    a = '10 is smaller than 10'
else:
    a = "no idea"

print(a)

y = 10

if y > 1:
    z = 'y is closest to 1'
elif y > 5:
    z = 'y is closest to 5'
elif y == 10:
    z = 'y is 10'
else:
    z = 'no idea'
print(z)

i = 7
if i < 10 and i > 5: # or
    print('this is true')
else:
    print("i does not fall in this range", i)


if (i > 5 and i < 10) or i > 100: # true if i 6, 7, 8, 9 or 101 and up
    if i != 7:
        print("this is true", i)

print(i > 5)
print(i < 10)
print((i > 5 and i < 10))
print(i >100)
print((i > 5 and i < 10) or i > 100)