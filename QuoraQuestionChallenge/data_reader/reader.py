import csv
import pandas as pd


class DataReader(object):
    def __init__(self, file_path):
        self.__file_path = file_path

        self.__all_train_data = []
        self.__all_train_labels = []
        self.__questions_ids = {}
        self.__data_id = {}

        self.__train_data, self.__train_labels = [], []
        self.__valid_data, self.__valid_labels = [], []
        self.__test_data, self.__test_labels = [], []

        self.__train_data_index_ptr = 0
        self.__valid_data_index_ptr = 0
        self.__test_data_index_ptr = 0

        self.__train_batch_index_ptr = 0
        self.__valid_batch_index_ptr = 0

    def get_all_train_data(self):
        df_train = pd.read_csv(self.__file_path)
        ids = df_train['id']
        q1_ids = list(df_train['qid1'])
        q2_ids = list(df_train['qid2'])
        questions1 = list(df_train['question1'])
        questions2 = list(df_train['question2'])
        is_duplicate = list(df_train['is_duplicate'])

        for i in range(0, len(ids)):
            self.__questions_ids[int(q1_ids[i])] = questions1[i]
            self.__questions_ids[int(q2_ids[i])] = questions2[i]
            self.__all_train_data.append((questions1[i], questions2[i]))
            self.__all_train_labels.append(int(is_duplicate[i]))
            self.__data_id[int(ids[i])] = (self.__all_train_data[-1], self.__all_train_labels[-1])

        return self.__all_train_data, self.__all_train_labels

    def get_train_data(self, size=0.8):
        target_length = int(size * len(self.__all_train_data))
        self.__train_data_index_ptr = target_length

        self.__train_data, self.__train_labels = self.__all_train_data[0:target_length], self.__all_train_labels[0:target_length]

        return self.__train_data, self.__train_labels

    def get_valid_data(self, size=0.1):
        self.__valid_data_index_ptr = self.__train_data_index_ptr + int(size * len(self.__all_train_data))

        self.__valid_data, self.__valid_labels = self.__all_train_data[self.__train_data_index_ptr:self.__valid_data_index_ptr], \
                                                 self.__all_train_labels[self.__train_data_index_ptr:self.__valid_data_index_ptr]

        return self.__valid_data, self.__valid_labels

    def get_test_data(self, size=0.1):
        self.__test_data_index_ptr = self.__valid_data_index_ptr + int(size * len(self.__all_train_data))

        self.__test_data, self.__test_labels = self.__all_train_data[self.__valid_data_index_ptr:], self.__all_train_labels[self.__valid_data_index_ptr:]

        return self.__test_data, self.__test_labels

    def get_train_next_batch(self, batch_size=10):
        old_ptr = self.__train_batch_index_ptr
        self.__train_batch_index_ptr += batch_size

        return self.__train_data[old_ptr:(old_ptr + batch_size)], self.__train_labels[old_ptr:(old_ptr + batch_size)] \
            if (old_ptr + batch_size) <= len(self.__train_labels) - 1 else None

    def get_valid_next_batch(self, batch_size=10):
        old_ptr = self.__train_batch_index_ptr
        self.__valid_batch_index_ptr += batch_size

        return self.__valid_data[old_ptr:(old_ptr + batch_size)], self.__valid_labels[old_ptr:(old_ptr + batch_size)] \
            if (old_ptr + batch_size) <= len(self.__valid_labels) - 1 else None

    def get_question_by_id(self, id):
        return self.__questions_ids[id] if id in self.__questions_ids else None

    def get_train_data_by_id(self, id):
        return self.__data_id[id] if id in self.__data_id else None