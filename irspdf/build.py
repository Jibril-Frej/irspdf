import pickle as pkl
from .ir_collection import IRCollection


def build(folder_path, pkl_path):
    """Builds and save a collection

    Args:
        folder_path: folder containing all pdf files used to build the
        collection

        pkl_path: pkl file were the collection will be saved

    """
    collection = IRCollection(folder_path)
    pkl.dump(collection, open(pkl_path, 'wb'))
