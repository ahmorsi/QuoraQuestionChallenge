

class Question(object):
    def __init__(self, question):
        self.__question = question
        self.__partial_questions = []
        self.__tokens = []
        self.__stemmed_question = ""
        self.__lemmatized_question = ""
        self.__stemmed_tokens = []
        self.__lemmatized_tokens = []
        self.__parse_tree_string = ""
        self.__tokens_tags = {}
        self.__tokens_chunks = {}
        self.__tokens_roles = {}

    def get_question(self):
        return self.__question

    def set_question_tokens(self, tokens):
        self.__tokens = tokens

    def get_question_tokens(self):
        return self.__tokens

    def set_stemmed_question_tokens(self, stemmed_tokens):
        self.__stemmed_tokens = stemmed_tokens
        self.__stemmed_question = ' '.join(stemmed_tokens)

    def get_stemmed_question(self):
        return self.__stemmed_question

    def get_stemmed_tokens(self):
        return self.__stemmed_tokens

    def set_lemmatized_question_tokens(self, lemmatized_tokens):
        self.__lemmatized_tokens = lemmatized_tokens
        self.__lemmatized_question = ' '.join(lemmatized_tokens)

    def get_lemmatized_question(self):
        return self.__lemmatized_question

    def get_lemmatized_tokens(self):
        return self.__lemmatized_tokens

    def set_partial_questions(self, partial_questions):
        self.__partial_questions = partial_questions

    def get_partial_questions(self):
        return self.__partial_questions

    def set_parse_tree_string(self, parse_tree_string):
        self.__parse_tree_string = parse_tree_string

    def get_parse_tree_string(self):
        return self.__parse_tree_string

    def set_tokens_tags(self, tokens_tags):
        self.__tokens_tags = tokens_tags

    def get_tokens_tags(self):
        return self.__tokens_tags

    def set_tokens_chunks(self, tokens_chunks):
        self.__tokens_chunks = tokens_chunks

    def get_tokens_chunks(self):
        return self.__tokens_chunks

    def set_tokens_roles(self, tokens_roles):
        self.__tokens_roles = tokens_roles

    def get_tokens_roles(self):
        return self.__tokens_roles

    def get_token_tag(self, index, token):
        return self.__tokens_tags[(index, token)]

    def get_token_chunk(self, index, token):
        return self.__tokens_chunks[(index, token)]

    def get_token_role(self, index, token):
        return self.__tokens_roles[(index, token)]