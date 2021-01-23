# a pipeline to vizualize word frequencies
import stanza, spacy, re, os
import matplotlib.pyplot as plt

def load_model(language):
    if language == "english":
        nlp = spacy.load('en_core_web_sm')
    elif language == "french":
        nlp = spacy.load("fr_core_news_sm")
    elif language == "chinese":
        nlp = spacy.load("zh_core_web_sm")
    elif language == "classical chinese":
        nlp = stanza.Pipeline('lzh')
    return nlp

def clean_spaces(text):
    # replace single new lines with space
    return re.sub('\n(?!\n)', " ", text)

def process_text(text, language, nlp):
    text = text.lower()
    text = clean_spaces(text)
    doc = nlp(text)

    if language == "classical chinese":
        words = [word.text for sentence in doc.sentences for word in sentence.words if word.text.isalnum()]
    elif language == "chinese":
        words = [word.text for word in doc if word.text.isalnum()]
    else:
        words = [word.lemma_ for word in doc if word.lemma_.isalnum()]

    return words

def load_corpus(directory, divider, language="english"):
    texts = []
    labels = []
    nlp = load_model(language)

    for root, dirs, files in os.walk(directory):
        for fname in files:
            if fname[0] != ".":
                with open(os.path.join(root, fname), "r", encoding='utf8') as rf:
                    #print(f"loading {fname}")
                    text = rf.read()
                    sections = re.split(divider, text, flags=re.M)[1:]
                    for i,section in enumerate(sections):
                        print(f"processsing section {i} of {fname}")
                        words = process_text(section, language, nlp)
                        texts.append(words)
                        labels.append(f"{i}_{fname[:-4]}")

    return texts, labels

def viz_term(term, texts, labels):
    term_counts = [words.count(term)/len(words) for words in texts]
    plt.xticks(rotation=90)
    plt.bar(labels, term_counts)
    plt.title(term)
    plt.show()

if __name__ == "__main__":
    eng_div = r'[IVX]+\.'
    chin_div = r'\n\s*第[一二三四五六七八九十百零]+卷'

    texts, labels = load_corpus('chinese', chin_div, 'chinese')

    # an improvement would be to put these on the same graph
    # viz_term("holmes", texts, labels)
    # viz_term("watson", texts, labels)
    # viz_term("crime", texts, labels)
    viz_term("仁", texts, labels)
