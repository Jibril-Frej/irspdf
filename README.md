# irspdf
A simple textual information retrieval system for pdf documents.

The ranking function used is BM25.

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
