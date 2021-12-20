import re
import os
import numpy as np
import pdfplumber
import snowballstemmer
from stop_words import get_stop_words
from collections import Counter, defaultdict


class IRCollection:
    """Builds a text IR collection from a set of pdf files.

    Attributes:
        max_length: max number of char in a valid word

        vocabulary: contains all the words in the collection

        inverted_index: inverted index of the collection

        doc_length: contains all the length of all the document

        avg_doc_length: average length of documents in the collection

        min_freq: min number of occurences for a word to be in the vocabulary

        idf: inverted document frequency of all words

        stops: set of stopwords to be deleterd from the vocabulary

        num_docs: total number of documents in the collection

    """
    def __init__(self, path=None):
        """Initialise max_length, min_freq and stops, if path is set to a
        value, builds the collection from the pdf files in the folder path

        """
        self.max_length = 30
        self.min_freq = 5
        self.stops = get_stop_words('en')
        self.stemmer = snowballstemmer.stemmer('english')
        if path:
            self.build_collection(path)

    def build_collection(self, path):
        """Builds the collection from the pdf files in the folder path

        Args:
            path: folder containing all pdf files used to build the collection

        """
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
                text = re.sub(r"[^a-zA-Z0-9,\-/]", " ", page.extract_text())
                for word in self.stemmer.stemWords(text.split()):
                    word = word.lower()
                    if (len(word) < self.max_length and len(word) > 1
                            and word not in self.stops):
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
        """Computes the smoothed idf of a single word

        Args:
            word: int of the associated word

        Returns: idf of word

        """
        return 1 + np.log((self.num_docs)/(1+len(self.inverted_index[word])))

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
        self.avg_doc_length = sum([val for val in self.doc_length.values()])
        self.avg_doc_length /= len(self.doc_length)

    def score_BM25(self, word_id, doc, freq, k1, b):
        """Computes the BM25 score of a term in a document

        Args:
            word_id: id of the word in the inverted index

            doc: document name

            freq: frequency of the word in the document

            k1: BM25 parameter must be a positive real value

            b: BM25 parameter must be in [0,1]


        Returns: The BM25 score

        """
        score = self.idf[word_id]*(k1+1)*freq
        score /= freq+k1*((1-b)+b*self.doc_length[doc]/self.avg_doc_length)
        return score

    def BM25(self, query, k1=1.2, b=0.75, k=1000, display=True):
        """Compute the BM25 score of all the documents with rtespect to a query

        Args:
            query: the query as a string

            k1: BM25 parameter must be a positive real value

            b: BM25 parameter must be in [0,1]

            k: max number of documents to return

            display: if set to true will print top-k document with their score


        Returns: A counter of the document and their BM25 score

        """
        query = re.sub(r"[^a-zA-Z0-9,\-/]", " ", query)
        results = Counter()
        for word in self.stemmer.stemWords(query.split()):
            word = word.lower()
            if word in self.vocabulary:
                word_id = self.vocabulary[word]
                for doc, freq in self.inverted_index[word_id]:
                    results[doc] += self.score_BM25(word_id, doc, freq, k1, b)
        if display:
            for doc, score in results.most_common(k):
                print(f'{doc} : {score}')
            if not results:
                print(f'Not document found for the query : {query}')
        return results

    def update(self, collection):
        """Updates the IRCollection with documents from a new IRCollection

        WARNING: The documents in the new IRCollection must be different from
        the documents in the original IRCollection

        Args:
            collection: IRCollection object that contains the documents to
            update to the collection with

        """
        nb_words = len(self.vocabulary)
        for word, index in collection.vocabulary.items():
            if word not in self.vocabulary:
                self.vocabulary[word] = nb_words
                self.inverted_index[nb_words] =\
                    collection.inverted_index[index]
                nb_words += 1
            else:
                oindex = self.vocabulary[word]
                self.inverted_index[oindex] += collection.inverted_index[index]

        for doc, length in collection.doc_length.items():
            self.doc_length[doc] = length

        self.avg_doc_length = sum([val for val in self.doc_length.values()])
        self.avg_doc_length /= len(self.doc_length)
        self.compute_idfs()
