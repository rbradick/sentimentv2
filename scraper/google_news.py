def scrape_google_news(query, max_results=10):
    import requests
    from bs4 import BeautifulSoup

    url = f"https://news.google.com/search?q={query}&hl=en-US&gl=US&ceid=US:en"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    articles = []

    for item in soup.find_all("article")[:max_results]:
        text = item.get_text()
        if text:
            articles.append(text.strip())

    return articles