# https://github.com/fxsjy/jieba
import jieba
import stanza
import spacy

# intall the model, this only needs to run once
# https://stanfordnlp.github.io/stanza/available_models.html
# stanza.download("lzh") # classical chinese
# stanza.download("zh-hant") # traditional chinese
# stanza.download("zh") # simplified chinese

# nlp = stanza.Pipeline('zh')


demo_sentence = "我的名字叫李友仁。"
english_sent = "Hello, his name is Paul and he runs"

# # words = list(jieba.cut(demo_sentence))

# # print(words)

# doc = nlp(demo_sentence)

# for sentence in doc.sentences:
#     for word in sentence.words:
#         if word.pos == "VERB":
#             print(word.text, word.pos)

nlp = spacy.load("zh_core_web_sm")
fren_nlp = spacy.load("fr_core_news_sm")
eng_nlp = spacy.load("en_core_web_sm")

doc = nlp(demo_sentence)
eng_doc = nlp(english_sent)
# spacy's model is only in a single layer
words = [word.text for word in doc]

eng_words = [word.lemma_ for word in eng_doc]

print(eng_words)