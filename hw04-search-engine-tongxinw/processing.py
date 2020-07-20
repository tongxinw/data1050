
import re
import string
import pytest
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize, sent_tokenize
from xml.etree import ElementTree

nltk.download('stopwords')

nltk.download('punkt')
# -

# regex for finding links
_LINK_RE = r'\[\[[^\[]+?\]\]'


def process_text(text, link_re=_LINK_RE):
    """Extracts lower-cased and stemmed tokens from input string and removes punctuation, stop
    words, and links ("[[...]]").

    1. Use `nltk.tokenize.sent_tokenize` and `.word_tokenize` for tokenizing
    2. Strip punctuations at both ends of words
    3. Stem words with the `stemmer`
    4. Filter stop words and empty words

    Use the given stemmer to stem each word. Use stop_words to filter out stop words.

    Args:
        text: str, one single str of text to be processed
        link_re: regular expression used to extract links. By default `_LINK_RE`

    Returns:
        list of str, tokenized & stemmed words.
    """
    english_stop_words = set(stopwords.words("english"))
    stemmer = PorterStemmer()
    text = re.sub(link_re, '', text)   # removes all links by substituting them with empty str
    # TODO: implement me
    # tokenize
    sentences = sent_tokenize(text)
    wordTokens = [word_tokenize(s) for s in sentences]
    words = [j for sub in wordTokens for j in sub]
    # remove punctuation
    words = [word.strip(string.punctuation) for word in words]
    # stem
    stemmed = [stemmer.stem(s) for s in words]
    # filter
    filtered = [x for x in stemmed if x not in english_stop_words]
    result = [x for x in filtered if x != '']
    return result


def extract_links(text, link_re=_LINK_RE):
    """
    Finds all occurrences of [[LINK]] or [[DISPLAY_TEXT|LINK]] in one single page.

    Args:
        text: str, one single str of text to be processed
        link_re: regular expression used to extract links. By default `_LINK_RE`

    Returns:
        A tuple of 2 elements
        1. a set of all the LINK part found in the text in lower case
        2. a string of all DISPLAY_TEXT or LINK itself if DISPLAY_TEXT is unavailable in lower case

    Example:
        "The [[Poland|Polish]] writer [[Bolesaw Prus]]"
        ==> (["polish", "bolesaw prus"],
            "poland bolesaw prus")
    """
    global _LINK_RE
    all_links = re.findall(link_re, text)
    linked_pages = set()
    link_text = []

    for l in all_links:
        # remove [[]]
        link = l.strip('[]')

        # process links that look like 'Washington|Presidents'
        # format is <text displayed>|<page linked to>
        c = link.count('|')
        if c > 1:
            # ignore [[File:XXX|aaa|bbb]], only handle 2-part links
            continue
        elif c == 1:
            split_link = link.split('|')
            link_text.append(split_link[0])
            linked_pages.add(split_link[1])
        else:
            link_text.append(link)
            linked_pages.add(link)

    return linked_pages, ' '.join(link_text)


def build_corpus(file_name):
    """
    Build a corpus by reading a XML file specified by `file_name`
    :param file_name: str
    :return:
        1. corpus, list of tuples. Each tuple is the title and content of a document (list of
        words)
        2. links, a dict mapping the title of a document to the titles all documents it links to
    :rtype: Tuple[Corpus, Links]
        Corpus := List[Tuple[str, List[str]]]
        Links := Dict[str, Set[str]]
    """
    tree = ElementTree.parse(file_name)
    root = tree.getroot()
    corpus = []
    links = {}
    for page in root.iter("page"):
        title = page.find("title").text.strip('\n')
        text = page.find("text").text
        suc, extra = extract_links(text)
        words = process_text(title + " " + text + extra)
        corpus.append((title, words))
        links[title] = suc
    return corpus, links


def test_processing_basic():
    assert extract_links("The [[Poland|Polish]] writer [[Bolesaw Prus]]") == (
        {"Polish", "Bolesaw Prus"}, "Poland Bolesaw Prus")
    assert process_text("These are some sample sentences. Watch out!") == ['sampl',
                                                                           'sentenc', 'watch']
    corpus, links = build_corpus('MiniWiki.xml')
    titles = [t for t, _ in corpus]
    assert sorted(titles) == ['Title 1', 'Title 2']
    assert links == {'Title 1': {'Title 2'}, 'Title 2': {'Title 1'}}
    print("PASS!")


def test_process_text():
    """Test for process_text"""
    assert process_text("Hello!! Thanksgiving~") == ['hello', 'thanksgiv']
    print("PASS!")


def test_build_corpus():
    """Test for build_corpus"""
    corpus, links = build_corpus("xiaoWiki.xml")

    assert links == {'Title 1': {'Title 2'}, 'Title 2': {'Title 1'}}
    assert corpus == [('Title 1', ['titl', '1', 'stem', 'remov', 'lot', 'noi', 'titl', '2']),
                      ('Title 2', ['titl', '2', 'thi', 'loop'])]
    print("PASS!")


test_processing_basic()
test_process_text()
test_build_corpus()

if __name__ == '__main__':
    # This will run all functions starting with `test_`
    pytest.main(['-v', __file__])
