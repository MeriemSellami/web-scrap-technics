# Web Scraping Example

This is a simple web scraping script using Python's `requests` library and `BeautifulSoup` for parsing HTML. The script fetches a webpage, extracts the content of the first `<h1>` header, the first `<p>` paragraph, and the first `<a>` link.

## Requirements

- Python
- `requests` library
- `beautifulsoup4` library

You can install the required libraries using pip:
```sh
pip install requests beautifulsoup4
```
## Usage
To run the script, simply execute it with Python:
```sh
python scrape.py
```
The script performs the following steps:

1.Sends a 'GET' request to the specified URL.


2.Parses the HTML content of the response.


3.Extracts and prints the text of the first 'h1' header.


4.Extracts and prints the text of the first 'p' paragraph.


5.Extracts and prints the href attribute of the first 'a' link.
