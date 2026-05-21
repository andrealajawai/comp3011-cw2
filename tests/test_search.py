from src.indexer import build_index
from src.search import print_word, find_query


def test_print_existing_word():
    index = build_index({"page1": "good friends"})
    result = print_word(index, "good")

    assert "page1" in result


def test_print_missing_word():
    index = build_index({"page1": "good friends"})
    result = print_word(index, "bad")

    assert result == "No results found for 'bad'."


def test_find_single_word():
    index = build_index({
        "page1": "good friends",
        "page2": "bad weather"
    })

    assert find_query(index, "good") == [("page1", 1)]


def test_find_multi_word_query():
    index = build_index({
        "page1": "good friends",
        "page2": "good weather"
    })

    assert find_query(index, "good friends") == [("page1", 2)]


def test_find_empty_query():
    index = build_index({"page1": "good friends"})

    assert find_query(index, "") == "Please enter a search query."


def test_find_nonexistent_word():
    index = build_index({
        "page1": "good friends"
    })

    assert find_query(index, "banana") == []


def test_print_empty_word():
    index = build_index({
        "page1": "good friends"
    })

    result = print_word(index, "")

    assert result == "Please enter a word to print."    