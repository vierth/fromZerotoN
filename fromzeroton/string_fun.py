# useful methods for dealing with strings
my_string = "Hello, how are you today, too?"

search_term = "to"
term_freq = my_string.count(search_term)

# print(term_freq)

# string concatenation
my_second_string = "Hello, friend!"
my_third_string = "How are you?"

combined_string = my_second_string + " " + my_third_string
#print(combined_string)

num_1 = "1234"
num_2 = "5678"
new_num = num_1 + num_2
#print(new_num)

# get the lenght of the string
#my_string_length = len(my_string)
#print(my_string_length)
#print(len(my_string))

# get first character
print(my_string[0])

# get last character
print(my_string[-1])

# get first ten characters
print(my_string[:10])

# characters 4 to 12
print(my_string[4:13])

# from charcter ten to the end
print(my_string[10:])

# find a substring
greeting = "Hello, my name is Paul! name"
result = greeting.find("how")
print(result)

# string replacement
a_o_mix = greeting.replace("au", "oo")
print(a_o_mix)
greeting = greeting.replace("au", "oo")
print(greeting)

# editing our string
lower_case_string = "this is a lower case string. no upper case here"
print(lower_case_string.capitalize())
print(lower_case_string.upper())
print(lower_case_string.lower())