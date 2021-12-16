# irspdf
A simple textual information retrieval system for pdf documents.

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
from irspdf import build_collection
build_collection(folder_path, collection_path)
```
folder_path : path of the folder that contains all the pdf files to include to the collection.

collection_path : file where the collection will be saved

### Query the collection

```
from irspdf import query_collection
query_collection(collection_path)
```
