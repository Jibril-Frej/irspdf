import sys
import pickle as pkl
from irspdf.collection import Collection


def main():
    collection = Collection()
    collection.build_collection(sys.argv[1])
    pkl.dump(collection, open(sys.argv[2], "wb"))


if __name__ == "__main__":
    main()
