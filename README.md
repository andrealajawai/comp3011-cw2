# COMP3011 Coursework 2 - Search Engine Tool

## Overview

This project is a search engine tool for COMP3011 Web Services and Web Data.

The search engine tool crawls the website https://quotes.toscrape.com/ which creates an inverted index of all words found on the pages. It also allows users to search for words and phrases from the stored index through a command-line interface.

---

## Project Structure

```text
data/
└── index.json

src/
├── __init__.py
├── crawler.py
├── indexer.py
├── search.py
└── main.py

tests/
├── test_crawler.py
├── test_indexer.py
└── test_search.py

.gitignore
README.md
requirements.txt
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/andrealajawai/comp3011-cw2.git
```

Move into the project directory:

```bash
cd comp3011-cw2
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Program

Run the search engine tool:

```bash
python -m src.main
```

---

## Commands

### Build the index

```text
build
```

Crawls the website and creates the inverted index.

---

### Load the index

```text
load
```

Loads the saved index from the filesystem.

---

### Print a word entry

```text
print <query>
```

Displays the inverted index entry for a word. Replace "<query>" with word of choice.

---

### Search for pages

```text
find <query1> <query2>
```

Returns pages containing all query words ranked by frequency. Replace "<query>" with word of choice.

---

## Testing

Run all tests:

```bash
python -m pytest
```

Run tests with coverage:

```bash
python -m pytest --cov=src
```