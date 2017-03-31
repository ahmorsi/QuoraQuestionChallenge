from data_reader.reader import DataReader
from libs_utils.sklearn_util.sklearn_util import SklearnUtil
from libs_utils.nltk_util.nltk_util import NltkUtil
from preprocessing_util.preprocessing import Preprocessing
import pickle


file_path = "./data/train.csv"

reader = DataReader(file_path)
reader.get_all_train_data()
questions_pairs, labels = reader.get_train_data()

preprocessor = Preprocessing(questions_pairs)
questions_pairs = preprocessor.remove_extra_whitespaces()
print("End removing extra spaces")

preprocessor = Preprocessing(questions_pairs)
questions_pairs = preprocessor.remove_punctuation()
print("End removing punctuations")

preprocessor = Preprocessing(questions_pairs)
questions_pairs = preprocessor.normalize_text()
print("End normalization")

preprocessor = Preprocessing(questions_pairs)
tokenized_questions_pairs = preprocessor.tokenize()
print("End tokenization")

preprocessor = Preprocessing(questions_pairs)
stemmed_questions_pairs = preprocessor.tokenize_with_stemming()
print("End stemmed tokenization")

preprocessor = Preprocessing(questions_pairs)
lemmatized_questions_pairs = preprocessor.tokenize_with_lemmatization()
print("End lemmatized tokenization")


print(questions_pairs[0])
print(tokenized_questions_pairs[0])
print(stemmed_questions_pairs[0])
print(lemmatized_questions_pairs[0])

with open('./stored_data/clean_question_pairs.pickle', "wb") as saver:
    pickle.dump(questions_pairs, saver, protocol=2)

with open('./stored_data/tokenized_question_pairs.pickle', "wb") as saver:
    pickle.dump(tokenized_questions_pairs, saver, protocol=2)

with open('./stored_data/stemmed_questions_pairs.pickle', "wb") as saver:
    pickle.dump(stemmed_questions_pairs, saver, protocol=2)

with open('./stored_data/lemmatized_questions_pairs.pickle', "wb") as saver:
    pickle.dump(lemmatized_questions_pairs, saver, protocol=2)