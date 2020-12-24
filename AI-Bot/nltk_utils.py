import nltk
nltk.download('punkt')
from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()

def tokenize(sentence):
    return nltk.word_tokenize(sentence)

def stem(word):
    return stemmer.stem(word.lower())

#Apply tokenizartion first 
def bag_of_words(tokenized_sentence, all_words):
    pass

# Testing the Tokenizeation and Stemming
a = 'How are you?'
print(a)
a= tokenize(a)
print(a)

words = ["Organize", "organized", "organizing"]
stemmed_words = [stem(w) for w in words]
print(stemmed_words)
