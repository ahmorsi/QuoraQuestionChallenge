from sklearn.feature_extraction.text import TfidfVectorizer
from collections import defaultdict


class SklearnUtil:
    @staticmethod
    def questions_vectorization(questions_pairs, n_gram_range=(1, 3)):
        questions_list = []

        for pair in questions_pairs:
            questions_list.append(pair[0])
            questions_list.append(pair[1])

        tfidf = TfidfVectorizer(analyzer='word', ngram_range=n_gram_range, min_df=0, stop_words='english')
        tfidf_matrix = tfidf.fit_transform(questions_list)

        print(tfidf_matrix)


