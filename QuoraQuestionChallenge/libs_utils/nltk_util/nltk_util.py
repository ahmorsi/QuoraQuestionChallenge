import nltk
from nltk.stem.porter import PorterStemmer

#nltk.download('punkt') #uncommend this to install the needed package

class NltkUtil:
    @staticmethod
    def tokenize(question):
        question_tokens = nltk.word_tokenize(question, language='english')
        stemmed_tokens = NltkUtil.stem(question_tokens)

        return stemmed_tokens

    @staticmethod
    def stem(tokens):
        return list(map(lambda v: PorterStemmer().stem(v), tokens))


