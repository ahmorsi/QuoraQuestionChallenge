from data_reader.reader import DataReader

file_path = "./data/train.csv"

reader = DataReader(file_path)
reader.get_all_train_data()
reader.get_train_data()
reader.get_train_next_batch()
