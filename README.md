# 🧠 Brand Sentiment Analysis App

This Streamlit app analyzes brand sentiment by scraping:
- Google News
- Tweets (via snscrape)
- Blogs (via Bing search)

## 🚀 Getting Started

### Install dependencies
```bash
pip install -r requirements.txt
```

### Run the app
```bash
streamlit run app.py
```

## 📂 Structure
- `app.py` - Main Streamlit UI
- `scraper/` - Scrapers for Google News, Twitter, and Blogs
- `sentiment/` - Sentiment analyzer using Hugging Face Transformers

## ✨ Output
The app displays a DataFrame of:
- Original Text
- Sentiment Label (POSITIVE/NEGATIVE)
- Confidence Score