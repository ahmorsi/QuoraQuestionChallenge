from libs_utils.nltk_util.nltk_util import NltkUtil
from libs_utils.sklearn_util.sklearn_util import SklearnUtil
from libs_utils.tensorflow_util import *
import re
import string


class Preprocessing(object):
    def __init__(self, questions_pairs):
        self.__questions_pairs = questions_pairs
        self.__words_id = {}
        self.__words_frequency = {}

    def tokenize_with_stemming(self):
        return list(map(lambda v: (NltkUtil.tokenize_with_stemming(v[0]), NltkUtil.tokenize_with_stemming(v[1])), self.__questions_pairs))

    def tokenize(self):
        return list(map(lambda v: (NltkUtil.tokenize(v[0]), NltkUtil.tokenize(v[1])), self.__questions_pairs))

    def tokenize_with_lemmatization(self):
        return list(map(lambda v: (NltkUtil.tokenize_with_lemmatization(v[0]), NltkUtil.tokenize_with_lemmatization(v[1])), self.__questions_pairs))

    def tokenize_with_lemmatization_and_stemming(self):
        return list(map(lambda v, u: (NltkUtil.tokenize_with_lemmatization_and_stemming(v), NltkUtil.tokenize_with_lemmatization_and_stemming(u)), self.__questions_pairs))

    def remove_extra_whitespaces(self):
        return list(map(lambda v: (re.sub('\s +', ' ', v[0]), re.sub('\s +', ' ', v[1])), self.__questions_pairs))

    def remove_punctuation(self):
        return list(map(lambda v: (v[0].translate(v[0].maketrans(string.punctuation, ' '*len(string.punctuation))).strip(), v[1].translate(v[1].maketrans(string.punctuation, ' '*len(string.punctuation))).strip()), self.__questions_pairs))

    def break_sentence(self):
        return list(map(lambda v, u: (NltkUtil.break_sentence(v), NltkUtil.break_sentence(u)), self.__questions_pairs))

    def normalize_text(self):
        return list(map(lambda v: (v[0].lower(), v[1].lower()), self.__questions_pairs))

