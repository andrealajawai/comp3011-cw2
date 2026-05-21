import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse


BASE_URL = "https://quotes.toscrape.com/"
POLITENESS_DELAY = 6


def is_valid_url(url):
    """Check that the URL belongs to the target website."""
    parsed_base = urlparse(BASE_URL)
    parsed_url = urlparse(url)

    return parsed_url.netloc == parsed_base.netloc


def get_page(url):
    """Fetch a page and return its HTML content."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.RequestException as error:
        print(f"Error fetching {url}: {error}")
        return None


def extract_text(html):
    """Extract visible quote text from the page."""
    soup = BeautifulSoup(html, "html.parser")

    texts = []

    for quote in soup.select(".quote"):
        quote_text = quote.select_one(".text")
        author = quote.select_one(".author")

        if quote_text:
            texts.append(quote_text.get_text(" ", strip=True))

        if author:
            texts.append(author.get_text(" ", strip=True))

    return " ".join(texts)


def extract_links(html, current_url):
    """Extract internal links from a page."""
    soup = BeautifulSoup(html, "html.parser")
    links = set()

    for link in soup.find_all("a", href=True):
        full_url = urljoin(current_url, link["href"])

        if is_valid_url(full_url):
            links.add(full_url)

    return links


def crawl_website(start_url=BASE_URL):
    """
    crawll quote pages using pagination only
    """
    visited = set()
    # to_visit = [start_url]
    pages = {}

    current_url = start_url
    
    while current_url and current_url not in visited:
        print(f"Crawling: {current_url}")
        html = get_page(current_url)

        if html is None:
            break
        
        text = extract_text(html)
        pages[current_url] = text
        
        visited.add(current_url)
        
        soup = BeautifulSoup(html, "html.parser")

        next_button = soup.select_one("li.next a")

        if next_button:
            next_url = urljoin(current_url, next_button["href"])
        else:
            next_url = None
        
        current_url = next_url

        #if current_url in visited:
        #    continue

        #print(f"Crawling: {current_url}")

        #html = get_page(current_url)

        #if html is None:
        #    visited.add(current_url)
        #    continue

        #text = extract_text(html)
        #pages[current_url] = text

        #visited.add(current_url)

        #new_links = extract_links(html, current_url)

        #for link in new_links:
        #    if link not in visited and link not in to_visit:
        #        to_visit.append(link)

        time.sleep(POLITENESS_DELAY)

    return pages