from src.indexer import tokenise


def print_word(index, word):
    """Return the inverted index entry for one word."""
    word = word.lower()

    if word not in index:
        return f"No results found for '{word}'."

    return index[word]


def find_query(index, query):
    """Find pages containing all words in the query."""
    words = tokenise(query)

    if not words:
        return "Please enter a search query."

    if any(word not in index for word in words):
        return []

    page_sets = []

    for word in words:
        page_sets.append(set(index[word].keys()))

    matching_pages = set.intersection(*page_sets)

    return sorted(matching_pages)