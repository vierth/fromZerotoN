# let's write a script that tells us the most common character in
# adventures of sherlock holmes.

with open("english/adventures_of_sherlock_holmes.txt", 'r', encoding="utf8") as rf:
    text = rf.read()

unique_characters = set(text)

# current most common character
most_common_character = []

# how often character occurs
character_freq = 0

# go through each character and count how often it occurs
for char in unique_characters:
    if char != " ":
        # get frequency
        freq = text.count(char)

        # check if freq is greater than character_freq
        if freq > character_freq:
            character_freq = freq
            most_common_character = [char]
        elif freq == character_freq:
            most_common_character.append(char)

print(f"The most common character is {most_common_character}, which occurs {character_freq} times.")
print(f"The length of this text is {len(text)}, with {len(unique_characters)} unique characters")