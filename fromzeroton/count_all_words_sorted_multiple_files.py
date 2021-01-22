import os

results = []

# let's iterate through every file in a directory
for root, dirs, files in os.walk('chinese'):
    files = [file_name for file_name in files if file_name[0] != "."]
    for file_name in files:
        file_path = os.path.join(root, file_name)
        with open(file_path, 'r', encoding='utf8') as rf:
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

        for word in sorted_words:
            results.append(f"{word},{word_frequencies[word]},{file_name[:-4]}")

with open('all_file_counts.csv', 'w', encoding='utf8') as wf:
    wf.write("\n".join(results))