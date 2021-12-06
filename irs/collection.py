import os
import numpy as np
import pdfplumber
from nltk import word_tokenize
from nltk.corpus import stopwords
from collections import Counter, defaultdict


class Collection:
    """Builds a text IR collection from a set of pdf files.

    Attributes:
        max_length: max number of char in a valid word
        vocabulary: contains all the words in the collection
        inverted_index: inverted index of the collection
        doc_length: contains all the length of all the document
        min_freq: min number of occurences for a word to be in the vocabulary
        idf: inverted document frequency of all words
        stops: set of stopwords to be deleterd from the vocabulary
        num_docs: total number of documents in the collection

    """
    def __init__(self, path):
        """init

        Args:
            path: folder containing all pdf files used to build the collection

        """
        self.max_length = 30
        self.min_freq = 5
        self.stops = set(stopwords.words('english'))
        self.vocabulary = Counter()
        self.read_all_pdfs(path)
        self.remove_low_freq()
        self.index_words()
        self.compute_idfs()
        self.compute_docs_lengths()

    def read_all_pdfs(self, path):
        """Extracts the text from all the pdf files in path

        Args:
            path: folder containing the pdf files

        """
        self.inverted_index = defaultdict(lambda: Counter())
        self.num_docs = 0
        for file in os.listdir(path):
            if '.pdf' in file:
                self.num_docs += 1
                self.read_pdf(os.path.join(path, file), file.split('.')[0])

    def read_pdf(self, path, docname):
        """Reads a single pdf file, builds a document from it and updates the
        vocabulary and the inverted index

        Args:
            path: pdf file location
            docname: name that will be given to the document

        """
        print(f"Reading {path} as {docname}")
        with pdfplumber.open(path) as pdf:
            for i, page in enumerate(pdf.pages):
                text = page.extract_text()
                text = word_tokenize(text)
                for word in text:
                    if (len(word) < self.max_length and len(word) > 1
                            and word.lower() not in self.stops):
                        self.inverted_index[word][docname] += 1
                        self.vocabulary[word] += 1

    def remove_low_freq(self):
        """Deletes from the vocabulary the words that occur less than min_freq
        times

        """
        for key in list(self.vocabulary.keys()):
            if self.vocabulary[key] < self.min_freq:
                del self.vocabulary[key]
                del self.inverted_index[key]

    def index_words(self):
        """Exchanges words in the vocabulary and the inverted index with int

        """
        for i, (key, value) in enumerate(self.vocabulary.most_common()):
            self.vocabulary[key] = i

        temp_inverted_index = dict()

        for key, value in self.vocabulary.items():
            temp_inverted_index[value] = self.inverted_index[key].most_common()
            del self.inverted_index[key]

        self.inverted_index = temp_inverted_index

    def get_idf(self, word):
        """Computes the idf of a single word

        Args:
            word: int of the associated word

        Returns: idf of word

        """
        return np.log((self.num_docs + 1)/(1+len(self.inverted_index[word])))

    def compute_idfs(self):
        """Compute the idf of all words in the vocabulary

        """
        self.idf = {word: self.get_idf(word) for word in self.inverted_index}

    def compute_docs_lengths(self):
        """Compute the length of all documents using the inverted index

        """
        self.doc_length = Counter()
        for words, posting_lists in self.inverted_index.items():
            for doc, freq in posting_lists:
                self.doc_length[doc] += freq
