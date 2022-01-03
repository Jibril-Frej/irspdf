import pickle as pkl
from .ir_collection import IRCollection


def update(folder_path, collection_path):
    """Builds and save a collection

    :param folder_path: folder containing all pdf files used to update the
        collection
    :type folder_path: str
    :param collection_path: Path of the collection file
    :type collection: str
    """
    collection = pkl.load(open(collection_path, "rb"))
    temp_collection = IRCollection(folder_path)
    collection.update(temp_collection)
    pkl.dump(collection, open(collection_path, 'wb'))
