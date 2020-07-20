"""
PageRankis a class which creates a search engine based on a link dictionary
"""
import pytest
import math


class PageRank:
    """
    An in-memory text search engine based on:
    a) The more documents that link to a page, the more authoritative it should be.
    b) The ability of an authoritative page to promote other pages should be constrained by the
       total number of outgoing links it has, fewer links provide better references.
    """

    def __init__(self, links, reverse_index, eps=1e-3, max_iter=500):
        """Creates a PageRank search engine based on links between pages.

        Args:
            links: A dict mapping the title of a page to all the pages it links to
                i.e. a dict of outgoing links
            reverse_index: A dict mapping each word to all the documents that contains this word,
                used in search
        """
        self.links = links
        self.reverse_index = reverse_index
        self.page_rank = self.calc_page_rank(self.links, eps, max_iter)

    @staticmethod
    def calc_page_rank(links, eps=1e-3, max_iter=50):
        """Calculates PageRank values for all pages. Stop iteration when the L2-distance between
        old/new weight is lower than `eps * N` or `max_iter` is reached.

        L2-norm is Euclidean distance between the old and the new weight vector of all pages.

        Args:
            links: A dict mapping the title of a page to all the pages it links to
                i.e. for each `v` in `links[u]`, there is an link from `u` to `v`
            eps: Stops iteration early when the L2 distance between old/new weight is lower
                than `eps * N`.
            max_iter: int, maximum number of iterations

        Returns:
            A mapping from page titles to their PageRank value.

        Examples:
            see `test_page_rank_basic`
        """
        # TODO: implement me
        weights = {}
        for x in links:
            weights[x] = 1/len(links)
#         print(weights)
        i = 1
        while i <= max_iter:
            new_weights = {}
            for x in links:
                new_weights[x] = 0
#             print('new_weights', new_weights)
            for x in links:
                count = 0
                for y in links[x]:
                    if y != x and y in links:
                        count += 1
#               print(count, x)
                if count == 0:
                    for e in new_weights:
                        new_weights[e] += weights[x]/len(links)
                else:
                    for y in links[x]:
                        if y != x and y in links:
                            new_weights[y] += weights[x]/count
#             print('new_weights', new_weights)
            sqr_sum = 0
            for page in weights:
                sqr_sum = weights[page]**2 + new_weights[page]**2
            dist = math.sqrt(sqr_sum)
            weights = new_weights
            i += 1
            if dist < eps*len(links):
                break
        return weights

    def search(self, keywords, limit=None):
        """Search for matching documents by keywords and calculate PageRank scores.

        Args:
            keywords: A list of terms. Each returned document contains at least one of the
                terms.
            limit: When a limit is specified, return at most that many pairs.

        Returns:
            A list of (document-title, PageRank) pairs. The results is sorted by PageRank score.
            When a limit is specified, only return that many pairs.
        """
        # TODO: implement me
        doc_list = []
        for word in keywords:
            docs = self.reverse_index[word]
            for doc in docs:
                doc_list.append(doc)
        doc_list = set(doc_list)
        pairs = []
        for doc in doc_list:
            pairs.append((doc, self.page_rank[doc]))
        pairs.sort(key=lambda tup: tup[1], reverse=True)
        if limit is None:
            return pairs
        elif len(pairs) >= limit:
            return pairs[:limit]
        else:
            return pairs


# +
def test_page_rank_basic():

    links = {"A": {"B"}, "B": {"C", "D"}, "C": {"B"}, "D": set()}
    reversed_index = {"hi": {"A", "B", "C", "D"}}
    pr = PageRank(links, reversed_index, max_iter=1)
    assert set(pr.search(["hi"])) == {
        ("B", 0.25 + 0.25 + 0.25 / 4),
        ("C", 0.25 / 2 + 0.25 / 4),
        ("D", 0.25 / 2 + 0.25 / 4),
        ("A", 0.25 / 4),
    }
    print("PASS!")


def test_calc_page_rank():
    """Test for calc_page_rank"""
    links = {"A": {"B", "C", "A"}, "B": set(), "C": {"A"}}
    p = PageRank.calc_page_rank(links, max_iter=4)
    assert sum(p.values()) == 1

    reversed_index = {"hi": {"A", "C"}, "here": {"B"}}
    pr = PageRank(links, reversed_index, max_iter=1)
    assert pr.search(['hi', "here"], 1) == [('A', 0.4444444444444444)]
    print("PASS!")


# -

test_page_rank_basic()
test_calc_page_rank()

if __name__ == '__main__':
    # This will run all functions starting with `test_`
    pytest.main(['-v', __file__])
