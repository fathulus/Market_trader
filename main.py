from market_data import fetch_ohlcv
from indicators import add_indicators
from generate_signal import generate_signal
from plotting import plot_price_and_indicators


def main():
    coins = ['bitcoin', 'ethereum', 'chainlink', 'ripple', 'cardano']

    for coin in coins:
        print(f"--- Analysis {coin.upper()} ---")
        df = fetch_ohlcv(symbol=coin, days='365', interval='daily')
        if df.empty:
            print(f" Lack of data for {coin}\n")
            continue

        df = add_indicators(df)
        latest = df.iloc[-1]

        print(f"[{latest.name}] Price: ${latest['price']:.2f}, RSI: {latest['rsi']:.2f}")
        signal = generate_signal(df)
        print(f"Signal: {signal}\n")

        plot_price_and_indicators(df, symbol=coin.upper())
        input("Press 'Enter' to display another plot of crypto")
if __name__ == "__main__":
    main()