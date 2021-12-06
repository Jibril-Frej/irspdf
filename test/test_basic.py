import sys
import pickle as pkl
from irs.collection import Collection


collection = Collection()
collection.build_collection(sys.argv[1])
pkl.dump(collection, open(sys.argv[2], "wb"))
