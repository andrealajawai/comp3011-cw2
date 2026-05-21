import json
import re


def tokenise(text):
    """Convert text into lowercase words."""
    return re.findall(r"\b[a-zA-Z]+\b", text.lower())


def build_index(pages):
    """Build an inverted index from crawled pages."""
    index = {}

    for url, text in pages.items():
        words = tokenise(text)

        for position, word in enumerate(words):
            if word not in index:
                index[word] = {}

            if url not in index[word]:
                index[word][url] = {
                    "frequency": 0,
                    "positions": []
                }

            index[word][url]["frequency"] += 1
            index[word][url]["positions"].append(position)

    return index


def save_index(index, filename="data/index.json"):
    """Save index to a JSON file."""
    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(index, file, indent=2)

    except Exception as error:
        print(f"Error saving index: {error}")


def load_index(filename="data/index.json"):
    """Load index from a JSON file."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    
    except FileNotFoundError:
        print("Index file not found.")
        return None
    
    except json.JSONDecodeError:
        print("Index file is corrupted.")
        return None