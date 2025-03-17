# Crypto Sentiment Analysis 📊💰

Analyze Reddit sentiment on cryptocurrencies and compare it with Bitcoin price movements over time.

---

## 📊 Features
- 🤖 Scrapes Reddit posts from **r/CryptoCurrency** using the Reddit API (`praw`)
- 🔍 Filters posts by keywords (e.g., Bitcoin, BTC, Ethereum)
- 🪨 Applies **sentiment analysis** using **VADER**
- 📈 Fetches **Bitcoin price data** from **CoinGecko API**
- 🌐 Visualizes sentiment vs BTC price trends

---

## 🛠️ Tech Stack
- Python 3.11+
- pandas, matplotlib
- praw (Reddit API client)
- vaderSentiment (sentiment scoring)
- requests (API calls)

---

## 📁 Project Structure
```
crypto-sentiment-analysis/
├── data/                        # CSV data files
│   ├── bitcoin_price_data.csv
│   ├── reddit_crypto_posts.csv
│   └── reddit_crypto_sentiment.csv
│
├── scripts/
│   ├── reddit_scraper.py        # Scrape Reddit + sentiment
│   └── price_fetcher.py         # Fetch BTC price data
│
├── notebooks/
│   └── sentiment_visualization.ipynb  # Plot sentiment vs price
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## 🚀 Quick Start
1. Clone this repo
2. Create a virtual environment
```bash
python -m venv venv
venv\Scripts\activate  # Windows
# OR
source venv/bin/activate  # macOS/Linux
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Set up Reddit API credentials [Guide](https://www.reddit.com/prefs/apps)
5. Run:
```bash
python scripts/reddit_scraper.py
python scripts/price_fetcher.py
```
6. Open Jupyter Notebook:
```bash
jupyter notebook notebooks/sentiment_visualization.ipynb
```

---

## 📊 Insights
- Observed Reddit sentiment fluctuates with market trends.
- Positive sentiment often precedes small BTC price upticks.
- Useful for **market mood tracking** and potential **price signal generation**.

---

## 🚀 Future Ideas
- Expand to other coins (ETH, SOL, etc.)
- Integrate **real-time dashboard** with Streamlit
- Predictive modeling: sentiment to price movements

---

## 💼 Author
**Ander Santamarta**  
Data Analyst / Data Scientist    

---

## 👀 License
Open-source project for demonstration and educational purposes.


