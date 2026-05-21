from src.indexer import tokenise, build_index


def test_tokenise_lowercase():
    assert tokenise("Hello, WORLD!") == ["hello", "world"]


def test_build_index_frequency():
    pages = {
        "page1": "good good friends",
        "page2": "good life"
    }

    index = build_index(pages)

    assert index["good"]["page1"]["frequency"] == 2
    assert index["good"]["page2"]["frequency"] == 1


def test_build_index_positions():
    pages = {
        "page1": "good friends good"
    }

    index = build_index(pages)

    assert index["good"]["page1"]["positions"] == [0, 2]