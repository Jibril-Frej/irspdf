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
from irspdf.collection import build_collection
build_collection(data_folder, collection_file)
```
data_folder : path of the folder that contains all the pdf files to include to the collection.

collection_file : file where the collection will be saved

### Query the collection

```
from irspdf.collection import query_collection
query_collection(collection_file)
```
