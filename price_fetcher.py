import requests
import pandas as pd
import os

def fetch_last_30_days(coin_id):
    url = f'https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart'
    params = {
        'vs_currency': 'usd',
        'days': '30',
        'interval': 'daily'
    }

    headers = {'User-Agent': 'Mozilla/5.0'}  # Avoid 401 issues
    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
        data = response.json()
        prices = data['prices']

        df = pd.DataFrame(prices, columns=['timestamp', 'price'])
        df['date'] = pd.to_datetime(df['timestamp'], unit='ms', utc=True).dt.date
        df.drop(columns='timestamp', inplace=True)

        os.makedirs('data', exist_ok=True)
        df.to_csv('data/bitcoin_price_data.csv', index=False)
        print("Saved to data/bitcoin_price_data.csv ✅")
        return df
    else:
        print(f"Error fetching data: {response.status_code}")
        return None

# Run it
btc_df = fetch_last_30_days('bitcoin')
if btc_df is not None:
    print(btc_df.head())



