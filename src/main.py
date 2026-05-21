from src.crawler import crawl_website
from src.indexer import build_index, save_index, load_index
from src.search import print_word, find_query


def main():
    index = None

    print("Search Engine Tool")
    print("Commands: build, load, print <word>, find <query>, quit")

    while True:
        command = input("> ").strip()

        if command == "quit":
            print("Goodbye.")
            break

        elif command == "build":
            pages = crawl_website()
            index = build_index(pages)
            save_index(index)
            print("Index built and saved.")

        elif command == "load":
            try:
                index = load_index()
                print("Index loaded.")
            except FileNotFoundError:
                print("No saved index found. Run build first.")

        elif command.startswith("print "):
            if index is None:
                print("Please run load or build first.")
            else:
                word = command[6:].strip()
                print(print_word(index, word))

        elif command.startswith("find "):
            if index is None:
                print("Please run load or build first.")
            else:
                query = command[5:].strip()
                print(find_query(index, query))

        else:
            print("Unknown command.")


if __name__ == "__main__":
    main()