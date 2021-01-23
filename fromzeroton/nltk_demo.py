import nltk

with open("english/adventures_of_sherlock_holmes.txt", 'r', encoding="utf8") as rf:
    text = rf.read()

text = text[text.find("*** START OF THIS PROJECT GUTENBERG EBOOK"):]
text = text[:text.find("*** END OF THIS PROJECT GUTENBERG EBOOK")]

# tokenize into sentences:
sentences = nltk.sent_tokenize(text)

# tokenize into words:
words = nltk.word_tokenize(text)

my_document = nltk.Text(words)

# my_document.concordance("Holmes", width=50, lines=25)
# my_document.dispersion_plot(["Holmes", "Watson"])
# my_document.collocations()

# get word frequencies
frequencies = nltk.FreqDist(my_document)
#print(frequencies['Holmes'])
most_common = frequencies.most_common(10)
print(most_common[0][1])

# print(frequencies.hapaxes())