import os
os.environ["STREAMLIT_SUPPRESS_CONFIG_WARNINGS"] = "true"
os.environ["STREAMLIT_DISABLE_LOGGING"] = "1"
os.environ["STREAMLIT_TELEMETRY_ENABLED"] = "0"

import streamlit as st
import pandas as pd

from scraper.google_news import scrape_google_news
from scraper.twitter_scraper import scrape_tweets
from scraper.blog_scraper import scrape_blogs
from sentiment.analyzer import analyze_sentiment

st.title("🧠 Brand Sentiment Analysis App")
brand = st.text_input("Enter a brand name to analyze", "Nike")

if st.button("Run Analysis"):
    st.write("🔍 Scraping data...")

    news_articles = scrape_google_news(brand)
    tweets = scrape_tweets(brand)
    blogs = scrape_blogs(brand)

    combined_articles = news_articles + tweets + blogs

    if combined_articles:
        st.success(f"✅ {len(combined_articles)} items scraped across all sources.")
        df = analyze_sentiment(combined_articles)
        st.dataframe(df)
    else:
        st.warning("No articles or posts found. Try another brand.")