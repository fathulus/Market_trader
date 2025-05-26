import pandas as pd



def generate_signal(df):
    """
Generates BUY, SELL, or HOLD signals based on the following indicators:
- RSI (14)
- SMA50 and SMA200 crossover (golden cross, death cross)
- MACD crossover

Assumption: df has the columns rsi, sma_50, sma_200, macd, macd_signal

Returns the signal for the last row of data.
    """
    if df.empty:
        return "HOLD"

    latest = df.iloc[-1]
    prev = df.iloc[-2] if len(df) > 1 else latest

    # RSI
    if not pd.isna(latest['rsi']):
        if latest['rsi'] > 70:
            return "SELL"
        elif latest['rsi'] < 30:
            return "BUY"

    # Intersection of SMA (Golden Cross / Death Cross)
    if not pd.isna(latest['sma_50']) and not pd.isna(latest['sma_200']) and not pd.isna(prev['sma_50']) and not pd.isna(prev['sma_200']):
        if prev['sma_50'] < prev['sma_200'] and latest['sma_50'] > latest['sma_200']:
            return "BUY"   # Golden Cross
        if prev['sma_50'] > prev['sma_200'] and latest['sma_50'] < latest['sma_200']:
            return "SELL"  # Death Cross

    # MACD crossover
    if not pd.isna(latest['macd']) and not pd.isna(latest['macd_signal']) and not pd.isna(prev['macd']) and not pd.isna(prev['macd_signal']):
        if prev['macd'] < prev['macd_signal'] and latest['macd'] > latest['macd_signal']:
            return "BUY"
        if prev['macd'] > prev['macd_signal'] and latest['macd'] < latest['macd_signal']:
            return "SELL"

    return "HOLD"