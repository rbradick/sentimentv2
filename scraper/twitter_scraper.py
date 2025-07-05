import snscrape.modules.twitter as sntwitter

def scrape_tweets(query, max_tweets=50):
    tweets = []
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(f'{query} lang:en').get_items()):
        if i >= max_tweets:
            break
        tweets.append(tweet.content)
    return tweets