import praw
import pandas as pd
from datetime import datetime, timedelta
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import os

# Ensure 'data/' folder exists
os.makedirs('data', exist_ok=True)

# ==== Fill in your Reddit API credentials ====
client_id = 'XbSge_kjxxzVvorwLXxxLQ'
client_secret = 'ZFVvck7DLG6kejk-10dGorun4NpAbw'
user_agent = 'crypto_scraper by u/Sad_Artist_6179'

# ==== Connect to Reddit ====
reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     user_agent=user_agent)

# ==== Scraper Settings ====
subreddit_name = 'CryptoCurrency'
search_keywords = ['bitcoin', 'btc', 'crypto', 'eth', 'ethereum']
days_back = 5        # Scrape last 5 days
limit = 50           # Up to 50 matching posts

# ==== Date Setup ====
start_date = datetime.utcnow() - timedelta(days=days_back)
start_timestamp = int(start_date.timestamp())

# ==== Scrape Posts ====
posts = []
print(f"\nFetching posts from r/{subreddit_name} (last {days_back} days)...\n")
for submission in reddit.subreddit(subreddit_name).new(limit=1000):
    post_time = datetime.utcfromtimestamp(submission.created_utc)
    if submission.created_utc >= start_timestamp:
        title = submission.title.lower()
        if any(keyword in title for keyword in search_keywords):
            posts.append({
                'date': post_time.date(),
                'title': submission.title,
                'content': submission.selftext,
                'score': submission.score,
                'url': submission.url
            })
            if len(posts) >= limit:
                break

# ==== Save Posts ====
df = pd.DataFrame(posts)
df.to_csv('data/reddit_crypto_posts.csv', index=False)
print(f"\nSaved {len(df)} posts to data/reddit_crypto_posts.csv ✅")

# ==== Sentiment Analysis ====
analyzer = SentimentIntensityAnalyzer()
df['full_text'] = df['title'] + ' ' + df['content']
df['sentiment'] = df['full_text'].apply(lambda text: analyzer.polarity_scores(text)['compound'])

# Save Sentiment CSV
df.to_csv('data/reddit_crypto_sentiment.csv', index=False)
print(f"Sentiment scores saved to data/reddit_crypto_sentiment.csv ✅")



