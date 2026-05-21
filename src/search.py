from src.indexer import tokenise


def print_word(index, word):
    """Return the inverted index entry for one word."""
    word = word.lower().strip()

    if not word:
        return "Please enter a word to print."

    if word not in index:
        return f"No results found for '{word}'."

    return index[word]


def find_query(index, query):
    """Find pages containing all words in the query."""
    words = tokenise(query)

    if not words:
        return "Please enter a search query."
    
    missing_words = [word for word in words if word not in index]
    if missing_words:
        return []
    
    page_sets = [set(index[word].keys()) for word in words]
    matching_pages = set.intersection(*page_sets)

    ranked_pages = []

    for page in matching_pages:
        score = 0

        for word in words:
            score += index[word][page]["frequency"]

        ranked_pages.append((page, score))

    ranked_pages.sort(key=lambda item: item[1], reverse=True)

    #if any(word not in index for word in words):
    #    return []

    #page_sets = []

    #for word in words:
    #    page_sets.append(set(index[word].keys()))

    #matching_pages = set.intersection(*page_sets)

    #return sorted(matching_pages)

    return ranked_pages