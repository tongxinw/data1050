"""
(This is a file-level docstring.)
This file provides a class that creates a TF-IDF search engine from a cleaned corpus.
"""
import math
import pytest  # noqa: F401; pylint: disable=unused-variable


class TFIDF:
    """An in-memory text search engine based on TF-IDF."""

    def __init__(self, corpus):
        """Creates a TF-IDF search engine on the corpus

        Args:
             corpus: A list of title-text tuples. Text is a list of terms found in a document.

        Examples:
            See `test_tfidf_basic`
        """
        self.corpus = corpus
        self.n_documents = len(corpus)
        # calculate the term frequency
        self.term_frequency = self.calc_term_frequency(corpus)
        # calculate tf-idf
        self.tf_idf = self.calc_tf_idf(self.term_frequency, self.n_documents)

    @staticmethod
    def calc_term_frequency(corpus):
        """Calculates the term frequency for all terms and documents in the corpus.

        Args:
            corpus: A list of (title, text) tuples. Each document has a `title` (a str) and a list
                a list of str as `text`.

        Returns:
            A dict containing the term frequencies for all terms and documents the corpus.

        Example:
            tf = TFIDF.calc_term_frequency([
                ('Document A', ['the', 'student', 'eats', 'the', 'apple']),
                ('Document B', ['the', 'apple', 'is', 'red']),
            ])
            assert tf['student']['Document A'] == 1 / 5
        """
        # (DONE)TODO: implement me
        word_dic = {}
        for item in corpus:
            title = item[0]
            text = item[1]
            d = {x: text.count(x) for x in text}
            for key in d.keys():
                if key not in word_dic:
                    word_dic[key] = {}
                word_dic[key][title] = d[key]/sum(d.values())
        return word_dic

    @staticmethod
    def calc_tf_idf(term_frequency, n_documents):
        """Calculates TF-IDF values for all terms and documents based on term frequency.

        Args:
            term_frequency: as returned by `calc_term_frequency`
            n_documents: the number of documents in the corpus

        Returns:
            TF-IDF values for all terms and documents.

        Examples:
            tf = TFIDF.calc_term_frequency(...)
            tf_idf = TFIDF.calc_tf_idf(tf, 2)
            assert tf_idf['student']['Document A'] == 1 / 5 * math.log(2 / 1)
        """
        d = term_frequency
        for key in d:
            docs = d[key]
            for doc in docs:
                value = docs[doc]
                docs[doc] = value * math.log(n_documents/len(docs))

        return d

    def search(self, keywords, limit=None):
        """Search for matching documents by keywords and calculate TF-IDF scores.
            Tf-idf score for a document is calculated by summing the tf-idf values of each query
            word found in the document.

        Args:
            keywords: A list of terms. Each returned document contains at least one of the
                terms.
            limit: When a limit is specified, return at most that many pairs.

        Returns:
            A list of (document-title, tf-idf) pairs. The results is sorted by TFIDF score.
            When a limit is specified, only return that many pairs.

        Examples:
            TFIDF(corpus).search(['student'], limit=1) == [('Document A', 1 / 5 * math.log(2 / 1))]
        """
        d = {}
        for key in keywords:
            for doc in self.tf_idf[key]:
                if doc not in d:
                    d[doc] = 0
                d[doc] += self.tf_idf[key][doc]
        l_1 = []
        for key in d:
            l_1.append((key, d[key]))
        l_1.sort(key=lambda tup: tup[1], reverse=True)
        if limit is None:
            return l_1
        elif len(l_1) >= limit:
            return l_1[:limit]
        else:
            return l_1


# +
def test_tfidf_basic():
    """Test basic functionality of TFIDF."""
    corpus = [('title 1', ['reinforcement', 'learning', 'is', 'learning', 'what', 'to', 'do']),
              ('title 2', ['reinforcement', 'learning', 'starts', 'with', 'interactive', 'agents'])]
    tf = TFIDF.calc_term_frequency(corpus)
    assert tf['learning'] == {'title 1': 2 / 7, 'title 2': 1 / 6}
    assert tf['to'] == {'title 1': 1 / 7}

    tf_idf = TFIDF.calc_tf_idf(tf, 2)
    assert tf_idf['reinforcement'] == {'title 1': 0, 'title 2': 0}
    assert tf_idf['agents'] == {'title 2': 1 / 6 * math.log(2 / 1)}

    engine = TFIDF(corpus)
    results = engine.search(['learning'])
    assert ('title 2', 0.0) in results
    assert ('title 1', 0.0) in results
    assert engine.search(['learning', 'agents'], 1) == [('title 2', 0.11552453009332421)]
    print("PASS!")


def test_tfidf():
    """More test cases for TFIDF class"""
    corpus = [('title 1', "hello word ha ha ha".split()),
              ('title 2', "what are your test cases".split()),
              ('title 3', "test test test for the 1050 class".split())]
    tf = TFIDF.calc_term_frequency(corpus)
    assert tf['test'] == {'title 2': 1 / 5, 'title 3': 3 / 7}

    tf_idf = TFIDF.calc_tf_idf(tf, len(corpus))
    assert tf_idf['test'] == {'title 2': 1 / 5 * math.log(3 / 2),
                              'title 3': 3 / 7 * math.log(3 / 2)}

    engine = TFIDF(corpus)
    assert engine.search(['test', "1050"])[0][1] == 1 / 7 * math.log(3) + 3 / 7 * math.log(3 / 2)
    assert engine.search([]) == []
    print("PASS!")


# -

test_tfidf_basic()
test_tfidf()

if __name__ == '__main__':
    # This will run all functions starting with `test_`
    pytest.main(['-v', __file__])




