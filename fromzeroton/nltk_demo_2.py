import nltk
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer

with open("english/adventures_of_sherlock_holmes.txt", 'r', encoding="utf8") as rf:
    text = rf.read()

#stemmer = SnowballStemmer('english')
lemmatizer = nltk.WordNetLemmatizer()

my_stopwords = stopwords.words("english")

text = text[text.find("*** START OF THIS PROJECT GUTENBERG EBOOK"):]
text = text[:text.find("*** END OF THIS PROJECT GUTENBERG EBOOK")]
text = text.lower()

# tokenize into sentences:
# sentences = nltk.sent_tokenize(text)

# tokenize into words:
words = nltk.word_tokenize(text)

# filtered_words = []
# for word in words:
#     if word.isalnum() and word not in my_stopwords:
#         filtered_words.append(word)

# filtered_words = [word for word in words if word.isalnum() and word not in my_stopwords]
filtered_words = [lemmatizer.lemmatize(word) for word in words if word.isalnum() and word not in my_stopwords]

unique_words = set(filtered_words)

lexical_diversity = len(unique_words)/len(filtered_words)

print(lexical_diversity)

my_document = nltk.Text(filtered_words)

# my_document.concordance("Holmes", width=50, lines=25)
# my_document.dispersion_plot(["Holmes", "Watson"])
# my_document.collocations()

# get word frequencies
frequencies = nltk.FreqDist(my_document)
#print(frequencies['Holmes'])
most_common = frequencies.most_common(10)
print(most_common)

# print(frequencies.hapaxes())