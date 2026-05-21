from src.crawler import crawl_website
from src.indexer import build_index, save_index, load_index
from src.search import print_word, find_query

def display_results(results):
    """Print search results in a readable format."""
    if isinstance(results, str):
        print(results)
    elif not results:
        print("No matching pages found.")
    else:
        print("Matching pages:")
        for page, score in results:
            print(f"- {page} (score: {score})")

def main():
    index = None

    print("COMP3011 CW2 - Search Engine Tool")
    print("Usable commands: build, load, print <word>, find <query>, quit")

    while True:
        command = input("> ").strip()

        if command == "quit":
            print("Goodbye! :)")
            break

        elif command == "build":
            pages = crawl_website()
            index = build_index(pages)
            save_index(index)
            print("Index built and saved.")

        elif command == "load":
            try:
                index = load_index()
                if index is not None:
                    print("Index loaded.")
            except FileNotFoundError:
                print("No saved index found. Please run build first!")

        elif command.startswith("print"):
            if index is None:
                print("Please run load or build first!")
            else:
                parts = command.split(maxsplit=1)

                if len(parts) < 2:
                    print("Please enter a word to print!")
                else:
                    print(print_word(index, parts[1]))

        elif command.startswith("find"):
            if index is None:
                print("Please run load or build first!")
            else:
                parts = command.split(maxsplit=1)

                if len(parts) < 2:
                    print("Please enter a search query!")
                else:
                    results = find_query(index, parts[1])
                    display_results(results)

        else:
            print("Unknown command.")


if __name__ == "__main__":
    main()