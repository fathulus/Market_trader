def add_indicators(df):
    from ta.momentum import RSIIndicator
    from ta.trend import SMAIndicator, EMAIndicator, MACD

    if 'price' not in df.columns:
        print("Lack of column 'price'.")
        return df

    df = df.copy()

    # RSI
    df['rsi'] = RSIIndicator(close=df['price'], window=14).rsi()

    # SMA & EMA
    df['sma_50'] = SMAIndicator(close=df['price'], window=50).sma_indicator()
    df['sma_200'] = SMAIndicator(close=df['price'], window=200).sma_indicator()
    df['ema_20'] = EMAIndicator(close=df['price'], window=20).ema_indicator()

    # MACD
    macd = MACD(close=df['price'])
    df['macd'] = macd.macd()
    df['macd_signal'] = macd.macd_signal()
    df['macd_diff'] = macd.macd_diff()

    # Volume (test)
    import numpy as np
    df['volume'] = np.random.randint(1000, 10000, size=len(df))

    return df