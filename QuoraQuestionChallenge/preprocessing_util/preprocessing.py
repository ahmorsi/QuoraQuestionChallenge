from libs_utils.nltk_util.nltk_util import NltkUtil
from libs_utils.sklearn_util.sklearn_util import SklearnUtil
from libs_utils.tensorflow_util import *
import re
import string

class Preprocessing(object):
    def __init__(self, questions):
        self.__questions = questions
        self.__words_id = {}
        self.__words_frequency = {}

    def tokenize_with_stemming(self):
        return list(map(lambda v: NltkUtil.tokenize_with_stemming(v), self.__questions))

    def tokenize(self):
        return list(map(lambda v: NltkUtil.tokenize(v), self.__questions))

    def tokenize_with_lemmatization(self):
        return list(map(lambda v: NltkUtil.tokenize_with_lemmatization(v), self.__questions))

    def tokenize_with_lemmatization_and_stemming(self):
        return list(map(lambda v: NltkUtil.tokenize_with_lemmatization_and_stemming(v), self.__questions))

    def remove_extra_whitespaces(self):
        return list(map(lambda v: re.sub('\s +', ' ', v), self.__questions))

    def remove_punctuation(self):
        return list(map(lambda v: v.translate(v.maketrans(string.punctuation, ' '*len(string.punctuation))).strip(), self.__questions))

    def break_sentence(self):
        return list(map(lambda v: NltkUtil.break_sentence(v), self.__questions))