from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

app = Flask(__name__)

def get_links(url):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        links = []
        for link in soup.find_all('a'):
            if 'href' in link.attrs:
                full_link = urljoin(url, link['href'])
                links.append(full_link)
        return links
    except:
        return []

def crawl(url, max_pages=100):
    parsed_url = urlparse(url)
    base_domain = parsed_url.netloc
    
    visited_pages = set()
    pages_to_visit = [url]
    found_pages = []

    while len(pages_to_visit) > 0 and len(found_pages) < max_pages:
        cur_page = pages_to_visit.pop(0)

        if cur_page in visited_pages:
            continue

        visited_pages.add(cur_page)
        found_pages.append(cur_page)

        new_links = get_links(cur_page)
        
        for link in new_links:
            link_domain = urlparse(link).netloc
            if link_domain == base_domain and link not in visited_pages:
                pages_to_visit.append(link)

    return found_pages

@app.route('/pages')
def crawl_request():
    url = request.args.get('target')
    
    if not url:
        return jsonify({"error": "No URL provided"}), 400

    try:
        pages = crawl(url)
        return jsonify({
            "domain": url,
            "pages": pages
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='localhost', port=8000, debug=True)
