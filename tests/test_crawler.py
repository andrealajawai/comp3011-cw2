from src.crawler import is_valid_url, extract_text, extract_links


def test_is_valid_url_accepts_target_site():
    assert is_valid_url("https://quotes.toscrape.com/page/1/") is True


def test_is_valid_url_rejects_external_site():
    assert is_valid_url("https://example.com/") is False


def test_extract_text_gets_quote_and_author():
    html = """
    <div class="quote">
        <span class="text">“Life is good.”</span>
        <small class="author">Andrea</small>
    </div>
    """

    result = extract_text(html)

    assert "Life is good" in result
    assert "Andrea" in result


def test_extract_links_gets_internal_links():
    html = """
    <a href="/page/2/">Next</a>
    <a href="https://example.com/">External</a>
    """

    links = extract_links(html, "https://quotes.toscrape.com/")

    assert "https://quotes.toscrape.com/page/2/" in links
    assert "https://example.com/" not in links