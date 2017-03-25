from data_reader.reader import DataReader
from libs_utils.sklearn_util.sklearn_util import SklearnUtil
from libs_utils.nltk_util.nltk_util import NltkUtil
from preprocessing_util.preprocessing import Preprocessing


file_path = "./data/train.csv"

reader = DataReader(file_path)
reader.get_all_train_data()
questions_pairs, labels = reader.get_train_data()