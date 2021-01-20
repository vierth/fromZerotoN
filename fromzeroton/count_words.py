# let's write a script that tells us the most common character in
# adventures of sherlock holmes.

with open("english/adventures_of_sherlock_holmes.txt", 'r', encoding="utf8") as rf:
    text = rf.read().lower()

# tokenize the text into words
words = text.split(" ")
print(words[100:110])
unique_word = set(words)

# current most common character
most_common_word = []

# how often character occurs
word_freq = 0

# go through each character and count how often it occurs
for word in unique_word:
    if word != "":
        # get frequency
        freq = words.count(word)

        # check if freq is greater than word_freq
        if freq > word_freq:
            word_freq = freq
            most_common_word = [word]
        elif freq == word_freq:
            most_common_word.append(word)

print(f"The most common character is {most_common_word}, which occurs {word_freq} times.")
print(f"The length of this text is {len(words)}, with {len(unique_word)} unique words")