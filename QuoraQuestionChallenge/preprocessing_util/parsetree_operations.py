from pattern.text.en import parsetree, parse
import pickle
from question import Question
import unicodedata

with open("./stored_data/lemmatized_questions_pairs.pickle", "rb") as loader:
    lemmatized_questions_pairs = pickle.load(loader)

with open("./stored_data/clean_question_pairs.pickle", "rb") as loader:
    clean_question_pairs = pickle.load(loader)

with open("./stored_data/stemmed_questions_pairs.pickle", "rb") as loader:
    stemmed_questions_pairs = pickle.load(loader)

with open("./stored_data/tokenized_question_pairs.pickle", "rb") as loader:
    tokenized_question_pairs = pickle.load(loader)

clean_question_pairs = map(lambda v: (v[0].encode('ascii', 'ignore'), v[1].encode('ascii', 'ignore')), clean_question_pairs)
lemmatized_questions_pairs = map(lambda v: (map(lambda u: u.encode('ascii', 'ignore'), v[0]), map(lambda u: u.encode('ascii', 'ignore'), v[1])), lemmatized_questions_pairs)
stemmed_questions_pairs = map(lambda v: (map(lambda u: u.encode('ascii', 'ignore'), v[0]), map(lambda u: u.encode('ascii', 'ignore'), v[1])), stemmed_questions_pairs)
tokenized_question_pairs = map(lambda v: (map(lambda u: u.encode('ascii', 'ignore'), v[0]), map(lambda u: u.encode('ascii', 'ignore'), v[1])), tokenized_question_pairs)


questions = []

for i in range(0, len(clean_question_pairs)):
    question1_string = clean_question_pairs[i][0]
    question2_string = clean_question_pairs[i][1]

    question1 = Question(question1_string)
    question2 = Question(question2_string)

    tokenized_question1 = tokenized_question_pairs[i][0]
    tokenized_question2 = tokenized_question_pairs[i][1]
    lemmatized_question1 = lemmatized_questions_pairs[i][0]
    lemmatized_question2 = lemmatized_questions_pairs[i][1]
    stemmed_question1 = stemmed_questions_pairs[i][0]
    stemmed_question2 = stemmed_questions_pairs[i][1]

    question1.set_lemmatized_question_tokens(lemmatized_question1)
    question2.set_lemmatized_question_tokens(lemmatized_question2)

    question1.set_stemmed_question_tokens(stemmed_question1)
    question2.set_stemmed_question_tokens(stemmed_question2)

    question1.set_question_tokens(tokenized_question1)
    question2.set_question_tokens(tokenized_question2)

    question1_parsetree = parsetree(question1_string)
    question2_parsetree = parsetree(question2_string)

    if len(question1_parsetree) == 1:
        parse_string = str(parse(question1_string, relations=True))
        question1.set_parse_tree_string(parse_string)
        tokens_tags, tokens_roles, tokens_chunks = {}, {}, {}

        for chunk in question1_parsetree[0]:
            for word in chunk.words:
                tokens_tags[(word.index, word.string)] = word.tag
                tokens_chunks[(word.index, word.string)] = word.chunk
                tokens_roles[(word.index, word.string)] = chunk.relations
                
                #TODO



s = ''
s = parse(s, relations=True)
print(s)
print(s.chunk)
for sentence in s:
    for chunk in sentence.chunks:
        for word in chunk.words:
            print(word.relations)


