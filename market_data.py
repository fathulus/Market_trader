import requests
import pandas as pd

def fetch_ohlcv(symbol='bitcoin', vs_currency='usd', days='365', interval='daily'):
    url = f'https://api.coingecko.com/api/v3/coins/{symbol}/market_chart'
    params = {
        'vs_currency': vs_currency,
        'days': days,
    }

    # CoinGecko pozwala tylko na 'daily'
    if interval and interval != 'daily':
        print(f" CoinGecko accepts only 'daily' like a interval. Avoid of interval='{interval}'")
    else:
        params['interval'] = interval

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
    except requests.RequestException as e:
        print(f"Error of downloading data: {e}")
        return pd.DataFrame()

    if 'prices' not in data:
        print("Lack of data in API:")
        print(data)
        return pd.DataFrame()

    # Konwersja do DataFrame
    df = pd.DataFrame(data['prices'], columns=['timestamp', 'price'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    df.set_index('timestamp', inplace=True)

    return df