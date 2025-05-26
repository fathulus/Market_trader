def rsi_signal(rsi):
    if rsi is None:
        return "WAIT"
    if rsi < 30:
        return "BUY"
    elif rsi > 70:
        return "SELL"
    else:
        return "WAIT"