from pattern.text.en import parsetree, parse
import pickle
from question import Question
import unicodedata
from itertools import chain

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

print(len(clean_question_pairs))
questions = []

def dic_to_string(param):
    string = ""

    for item in param.items():
        string += str(item[0][0]) + " " + str(item[0][1]) + " " + str(item[1]) + " "

    return string.strip()

for i in range(40000, 50000):
    print(i)
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

    question1_parsetree = parsetree(question1_string, relations=True)
    question2_parsetree = parsetree(question2_string, relations=True)

    if len(question1_parsetree) == 1:
        parse_string = str(parse(question1_string, relations=True))
        question1.set_parse_tree_string(parse_string)
        tokens_tags, tokens_roles, tokens_chunks = {}, {}, {}

        for sentence in question1_parsetree:
            for chunk in sentence.chunks:
                for word in chunk.words:
                    #print(chunk.role)
                    tokens_tags[(int(word.index), str(word.string))] = word.tag
                    tokens_chunks[(int(word.index), str(word.string))] = word.chunk
                    tokens_roles[(int(word.index), str(word.string))] = chunk.role

        question1.set_tokens_tags(tokens_tags)
        question1.set_tokens_chunks(tokens_chunks)
        question1.set_tokens_roles(tokens_roles)

    else:
        parse_string = str(parse(question1_string, relations=True))
        question1.set_parse_tree_string(parse_string)
        tokens_tags, tokens_roles, tokens_chunks = {}, {}, {}

        for sentence in question1_parsetree:
            for chunk in sentence.chunks:
                for word in chunk.words:
                    tokens_tags[(int(word.index), str(word.string))] = word.tag
                    tokens_chunks[(int(word.index), str(word.string))] = word.chunk
                    tokens_roles[(int(word.index), str(word.string))] = chunk.role

        question1.set_tokens_tags(tokens_tags)
        question1.set_tokens_chunks(tokens_chunks)
        question1.set_tokens_roles(tokens_roles)

        partial_questions = []

        for partial_question in question1_parsetree[1:]:
            partial_question_string = partial_question.string
            partial_question_object = Question(partial_question_string)

            parse_string = str(parse(partial_question_string, relations=True))
            partial_question_parse_tree = parsetree(partial_question_string, relations=True)
            partial_question_object.set_parse_tree_string(parse_string)
            tokens_tags, tokens_roles, tokens_chunks = {}, {}, {}

            for sentence in partial_question_parse_tree:
                for chunk in sentence.chunks:
                    for word in chunk.words:
                        tokens_tags[(int(word.index), str(word.string))] = word.tag
                        tokens_chunks[(int(word.index), str(word.string))] = word.chunk
                        tokens_roles[(int(word.index), str(word.string))] = chunk.role

            partial_question_object.set_tokens_tags(tokens_tags)
            partial_question_object.set_tokens_chunks(tokens_chunks)
            partial_question_object.set_tokens_roles(tokens_roles)

            partial_questions.append(partial_question_object)

        question1.set_partial_questions(partial_questions)

    if len(question2_parsetree) == 1:
        parse_string = str(parse(question1_string, relations=True))
        question2.set_parse_tree_string(parse_string)
        tokens_tags, tokens_roles, tokens_chunks = {}, {}, {}

        for sentence in question2_parsetree:
            for chunk in sentence.chunks:
                for word in chunk.words:
                    tokens_tags[(int(word.index), str(word.string))] = word.tag
                    tokens_chunks[(int(word.index), str(word.string))] = word.chunk
                    tokens_roles[(int(word.index), str(word.string))] = chunk.role

        question2.set_tokens_tags(tokens_tags)
        question2.set_tokens_chunks(tokens_chunks)
        question2.set_tokens_roles(tokens_roles)

    else:
        parse_string = str(parse(question2_string, relations=True))
        question2.set_parse_tree_string(parse_string)
        tokens_tags, tokens_roles, tokens_chunks = {}, {}, {}

        for sentence in question2_parsetree:
            for chunk in sentence.chunks:
                for word in chunk.words:
                    tokens_tags[(int(word.index), str(word.string))] = word.tag
                    tokens_chunks[(int(word.index), str(word.string))] = word.chunk
                    tokens_roles[(int(word.index), str(word.string))] = chunk.role

        question2.set_tokens_tags(tokens_tags)
        question2.set_tokens_chunks(tokens_chunks)
        question2.set_tokens_roles(tokens_roles)

        partial_questions = []

        for partial_question in question2_parsetree[1:]:
            partial_question_string = partial_question.string
            partial_question_object = Question(partial_question_string)

            parse_string = str(parse(partial_question_string, relations=True))
            partial_question_parse_tree = parsetree(partial_question_string, relations=True)
            partial_question_object.set_parse_tree_string(parse_string)
            tokens_tags, tokens_roles, tokens_chunks = {}, {}, {}

            for sentence in partial_question_parse_tree:
                for chunk in sentence.chunks:
                    for word in chunk.words:
                        tokens_tags[(int(word.index), str(word.string))] = word.tag
                        tokens_chunks[(int(word.index), str(word.string))] = word.chunk
                        tokens_roles[(int(word.index), str(word.string))] = chunk.role

            partial_question_object.set_tokens_tags(tokens_tags)
            partial_question_object.set_tokens_chunks(tokens_chunks)
            partial_question_object.set_tokens_roles(tokens_roles)

            partial_questions.append(partial_question_object)

        question2.set_partial_questions(partial_questions)

    questions.append((question1, question2))

print("End Processing")

q = questions[0][0]

with open("./stored_data/data_preprocessing.txt", "a") as writer:
    for question_pair in questions:
        writer.write("#\n")

        first_question = question_pair[0]
        second_question = question_pair[1]

        writer.write(first_question.get_question() + "\n")
        writer.write(' '.join(first_question.get_question_tokens()) + "\n")
        writer.write(first_question.get_stemmed_question() + "\n")
        writer.write(' '.join(first_question.get_stemmed_tokens()) + "\n")
        writer.write(first_question.get_lemmatized_question() + "\n")
        writer.write(' '.join(first_question.get_lemmatized_tokens()) + "\n")
        writer.write(dic_to_string(first_question.get_tokens_tags()) + "\n")
        writer.write(dic_to_string(first_question.get_tokens_roles()) + "\n")
        writer.write(dic_to_string(first_question.get_tokens_chunks()) + "\n")

        partial_first_question = first_question.get_partial_questions()
        writer.write(str(len(partial_first_question)) + "\n")

        for i in range(0, len(partial_first_question)):
            current_question = partial_first_question[i]
            writer.write(current_question.get_question() + "\n")
            writer.write(' '.join(current_question.get_question_tokens()) + "\n")
            writer.write(current_question.get_stemmed_question() + "\n")
            writer.write(' '.join(current_question.get_stemmed_tokens()) + "\n")
            writer.write(current_question.get_lemmatized_question() + "\n")
            writer.write(' '.join(current_question.get_lemmatized_tokens()) + "\n")
            writer.write(dic_to_string(current_question.get_tokens_tags()) + "\n")
            writer.write(dic_to_string(current_question.get_tokens_roles()) + "\n")
            writer.write(dic_to_string(current_question.get_tokens_chunks()) + "\n")

        writer.write("--\n")

        writer.write(second_question.get_question() + "\n")
        writer.write(' '.join(second_question.get_question_tokens()) + "\n")
        writer.write(second_question.get_stemmed_question() + "\n")
        writer.write(' '.join(second_question.get_stemmed_tokens()) + "\n")
        writer.write(second_question.get_lemmatized_question() + "\n")
        writer.write(' '.join(second_question.get_lemmatized_tokens()) + "\n")
        writer.write(dic_to_string(second_question.get_tokens_tags()) + "\n")
        writer.write(dic_to_string(second_question.get_tokens_roles()) + "\n")
        writer.write(dic_to_string(second_question.get_tokens_chunks()) + "\n")

        partial_second_question = second_question.get_partial_questions()
        writer.write(str(len(partial_second_question)) + "\n")

        for i in range(0, len(partial_second_question)):
            current_question = partial_second_question[i]
            writer.write(current_question.get_question() + "\n")
            writer.write(' '.join(current_question.get_question_tokens()) + "\n")
            writer.write(current_question.get_stemmed_question() + "\n")
            writer.write(' '.join(current_question.get_stemmed_tokens()) + "\n")
            writer.write(current_question.get_lemmatized_question() + "\n")
            writer.write(' '.join(current_question.get_lemmatized_tokens()) + "\n")
            writer.write(dic_to_string(current_question.get_tokens_tags()) + "\n")
            writer.write(dic_to_string(current_question.get_tokens_roles()) + "\n")
            writer.write(dic_to_string(current_question.get_tokens_chunks()) + "\n")




print("Question: " + str(q.get_question()))
print("Tokens: " + str(q.get_question_tokens()))
print("Stemmed Question: " + str(q.get_stemmed_question()))
print("Stemmed Tokens: " + str(q.get_stemmed_tokens()))
print("Lemmatized Question" + str(q.get_lemmatized_question()))
print("Lemmatized Tokens" + str(q.get_lemmatized_tokens()))
print("Partial Questions: " + str(q.get_partial_questions()))
print("Parsetree String: " + str(q.get_parse_tree_string()))
print("Tokens Tags: " + str(q.get_tokens_tags()))
print("Tokens Roles: " + str(q.get_tokens_roles()))
print("Tokens Chunks" + str(q.get_tokens_chunks()))



"""
with open('./stored_data/questions_objects_pairs.pickle', "wb") as saver:
    pickle.dump(questions, saver, protocol=2)


s = 'What is the step by step guide to invest in share market in india?'
s = parsetree(s, relations=True)

for sentence in s:
    for chunk in sentence.chunks:
        for word in chunk.words:
            print(str(word.string) + " " + str(chunk.role))


"""