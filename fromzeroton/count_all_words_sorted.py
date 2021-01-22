# let's count all of the words that occur in a document
with open('english/adventures_of_sherlock_holmes.txt', 'r', encoding='utf8') as rf:
    text = rf.read()

# make the text lower case
text = text.lower()
# replace new line with a space
text = text.replace("\n", " ")

things_to_delete = [",", ".", "?", "!", "'", "\"", "“", "”"]
for thing_to_delete in things_to_delete:
    text = text.replace(thing_to_delete, "")

words = text.split(" ")
unique_words = set(words)

# create a dictionary to save word frequencies
word_frequencies = {}

for word in unique_words:
    if word != "":
        word_count = words.count(word)
        word_frequencies[word] = word_count

sorted_words = sorted(word_frequencies, key=word_frequencies.get, reverse=True)

with open('word_count_results.csv', 'w', encoding='utf8') as wf:
    for word in sorted_words:
        wf.write(f"{word},{word_frequencies[word]}\n")