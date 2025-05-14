# Web Crawler

A web crawler that returns all pages within the same domain.

## Features

- Website crawling within the same domain.
- Returns a JSON response with all discovered pages
- Limits crawling to 100 pages by default
- Handles basic error cases.

## Requirements:

- Python 3
- Flask
- Requests
- BeautifulSoup

## Installation

1. Clone the repository
2. Install the required packages using:
```bash
pip3 install -r requirements.txt
```

## Usage

1. Start the server:
```bash
python3 main.py
```

The server will start on `http://localhost:8000`

3. Make a GET request to `/pages` with a `target` parameter

example:
```bash
curl "http://localhost:8000/pages?target=https://example.com"
```

## Response example:

```json
{
    "domain": "https://example.com",
    "pages": [
        "https://example.com"
    ]
}
```

## Error response examples:

```json
{
    "error": "No URL provided"
}
```

```json
{
    "error": "error message details"
}
```

## Error handling

- Missing URL parameter
- Parsing errors