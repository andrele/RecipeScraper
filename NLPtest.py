import nltk
from nltk.tokenize import word_tokenize
sentence = "butter, tart apples - peeled, cornstarch, cold water, brown sugar, ground cinnamon"
tokens = nltk.word_tokenize(sentence)
print(tokens)
tagged = nltk.pos_tag(tokens)
print(tagged)