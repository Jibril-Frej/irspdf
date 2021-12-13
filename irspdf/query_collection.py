import sys
import pickle as pkl


def main():
    collection = pkl.load(open(sys.argv[1], "rb"))
    query = input("Enter your query (enter exit to leave) :")
    while query != "exit":
        collection.BM25(query)
        query = input("Enter your query (enter exit to leave) :")


if __name__ == "__main__":
    main()
