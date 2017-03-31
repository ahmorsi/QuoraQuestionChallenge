import nltk
from nltk.stem.porter import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
#nltk.download('wordnet') #uncommend this to install the needed package


class NltkUtil:
    @staticmethod
    def tokenize(question):
        return nltk.word_tokenize(question, language='english')

    @staticmethod
    def tokenize_with_stemming(question):
        question_tokens = nltk.word_tokenize(question, language='english')
        stemmed_tokens = NltkUtil.stem(question_tokens)

        return stemmed_tokens

    @staticmethod
    def tokenize_with_lemmatization(question):
        question_tokens = nltk.word_tokenize(question, language='english')
        lemmatized_tokens = NltkUtil.lemmatize(question_tokens)

        return lemmatized_tokens

    @staticmethod
    def tokenize_with_lemmatization_and_stemming(question):
        question_tokens = nltk.word_tokenize(question, language='english')
        stemmed_tokens = NltkUtil.stem(question_tokens)
        lemmatized_tokens = NltkUtil.lemmatize(stemmed_tokens)

        return lemmatized_tokens

    @staticmethod
    def stem(tokens):
        return list(map(lambda v: PorterStemmer().stem(v), tokens))

    @staticmethod
    def lemmatize(tokens):
        return list(map(lambda v: WordNetLemmatizer().lemmatize(v), tokens))

    @staticmethod
    def lexical_parse(question_tokens):
        pass

    @staticmethod
    def break_sentence(question):
        return nltk.sent_tokenize(question, language='english')

