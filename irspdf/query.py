import pickle as pkl


def query(collection_path):
    """Reads the collection and print the documents ranked by relevance with
    respect to the query

    Args:
        collection_path: Path of the collection file

    """
    collection = pkl.load(open(collection_path, "rb"))
    query = input("Enter your query (enter $exit to leave) :")
    while query != "$exit":
        collection.BM25(query)
        query = input("Enter your query (enter exit to leave) :")
