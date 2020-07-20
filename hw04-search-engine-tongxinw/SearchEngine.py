"""
SearchEngine is a class which determines search engines. 
"""
from processing import build_corpus, process_text
from PageRank import PageRank
from TFIDF import TFIDF


class SearchEngine:
    """
    SearchEngine determines certain search engine based on the user's choice and returns the score of query words.
    """
    def __init__(self, file_name):
        """Creates a search engine backed by PageRank and TF-IDF

        Args:
            file_name: path to xml files of wiki dump
        """
        # build corpus from xml files
        self.corpus, self.links = build_corpus(file_name)
        self.tf_idf = TFIDF(self.corpus)
        print("TFIDF engine has started")
        self.reverse_index = {word: set(mapping.keys())
                              for word, mapping in self.tf_idf.tf_idf.items()}
        self.page_rank = PageRank(self.links, self.tf_idf.tf_idf)
        print("PageRank engine has started")

    def search(self, query, mode, limit=10):
        """Sends `process_text(query)` to the search engines selected by `mode` and returns article
            titles and associated scores up to `limited`. Results are sorted by their scores in
            a descending order.

        Args:
            query: raw query string
            mode: 'TF-IDF|PageRank|smart'
            limit: int

        Returns:
            A list of tuples. Each tuple is a document title and score pair.
        """
        keywords = process_text(query)  # process a raw query string to a cleaner version, remove
        # all the punctuations and white spaces
        if mode == 'TF-IDF':
            return self.tf_idf.search(keywords, limit)
        elif mode == 'PageRank':
            return self.page_rank.search(keywords, limit)
        elif mode == 'smart':
            return self.smart_search(keywords, limit)
        raise ValueError('Undefined search mode')

    def smart_search(self, keywords, limit=None):
        """
        Returns the score of certain query words based on TFIDF score and pagerank score. 
        """
        smart_scores = {}
        tf_idf = self.tf_idf.tf_idf
        page_rank = self.page_rank.page_rank
        for word in keywords:
            if word in self.reverse_index:
                for page in self.reverse_index[word]:
                    if page not in smart_scores:
                        smart_scores[page] = 0
                    smart_scores[page] += tf_idf[word][page] + page_rank[page]
        result = sorted(smart_scores.items(), key=lambda x: x[1], reverse=True)
        return result[:limit]


