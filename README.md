# irspdf
A simple textual information retrieval system for pdf documents.

Standard text preprocessing for information retrieval is applied:
* StopWord removal
* Stemming 
* Punctuation removal
* Lowercase conversion

The ranking function used is BM25 :

$$ BM25(q, d) = \sum_{t \in q}idf_t \cdot \frac{tf_{t,d}\cdot(k_1 + 1)}{tf_{t,d} + k_1 \cdot((1-b)\cdot\frac{|d|}{avgdl}) } $$

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
