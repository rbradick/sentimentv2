import requests
from bs4 import BeautifulSoup

def scrape_blogs(query, max_results=10):
    blogs = []
    search_url = f"https://www.bing.com/search?q={query}+blog&count={max_results}"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    results = soup.find_all("li", class_="b_algo")

    for result in results:
        snippet = result.find("p")
        if snippet:
            blogs.append(snippet.text)
    return blogs