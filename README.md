# irspdf
A simple textual information retrieval system for pdf documents.

Text is extracted from pdf with pdfplumber.

Standard text preprocessing for information retrieval is applied:
* StopWord removal
* Stemming 
* Punctuation removal
* Lowercase conversion

The ranking function used is BM25.

## Documentation

Documentation can be found at [https://irspdf.readthedocs.io/en/latest/](https://irspdf.readthedocs.io/en/latest/).

## Installation

### Install with pip
```
pip install irspdf
```

### OR install from github
```
git clone https://github.com/Jibril-Frej/irspdf.git
cd irspdf && python setup.py install
```

## Usage

### Build a collection

```
from irspdf import build
build(folder_path, collection_path)
```
folder_path : path of the folder that contains all the pdf files to include to the collection.

collection_path : file where the collection will be saved

### Query the collection

```
from irspdf import query
query(collection_path)
```

collection_path : file where the collection is saved

### Update the collection

```
from irspdf import update
update(folder_path, collection_path)
```

folder_path : path of the folder that contains all the pdf files to add to the collection.

collection_path : file where the original collection is saved
