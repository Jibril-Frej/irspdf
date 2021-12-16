import pickle as pkl
from .collection import Collection


def build_collection(folder_path, pkl_path):
    """Builds and save a collection

    Args:
        folder_path: folder containing all pdf files used to build the
        collection

        pkl_path: pkl file were the collection will be saved

    """
    collection = Collection()
    collection.build_collection(path=folder_path)
    pkl.dump(collection, open(pkl_path, 'wb'))
